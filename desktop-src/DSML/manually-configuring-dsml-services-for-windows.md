---
title: Manually Configuring DSML Services for Windows
description: The following procedure shows how to manually configure DSML Services for Windows. Manual configuration is performed to support multiple installations of DSML Services for Windows on the same IIS server.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: '01482a0e-c7c0-425f-992d-0abbff8a7b2f'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-domain-services'
ms.tgt_platform: multiple
keywords: ["Configuring DSML Services for Windows Manually DSML"]
---

# Manually Configuring DSML Services for Windows

The following procedure shows how to manually configure DSML Services for Windows. Manual configuration is performed to support multiple installations of DSML Services for Windows on the same IIS server.

Before manually configuring DSML services for Windows, [install DSML Services for Windows](installing-dsml-services-for-windows.md). Also ensure that IIS and Active Directory are installed and configured on the server.

**To manually configure DSML Services for Windows**

1.  [Create the DSML virtual directory](#create-the-dsml-virtual-directory)
2.  [Configure the DSML virtual directory](#configure-the-dsml-virtual-directory)
3.  [Modify the DSML configuration file](#modify-the-dsml-configuration-file)
4.  [Test the DSML configuration](#test-the-dsml-configuration)

## Create the DSML virtual directory

A new DSML virtual directory is created on the IIS web server.

**To create the DSML virtual directory**

1.  Start IIS services and create a new virtual directory named **dsml** on the web server under the **Default Web Site**, with the path to directory set to C:\\dsfw\\bin (or to the directory created during setup).
2.  Set the **Execute Permissions** of the virtual directory to **Scripts and Executables**.

## Configure the DSML virtual directory

The DSML virtual directory security is set as specified. In addition, a mapping to Adssoap.dll is added.

**To configure the DSML virtual directory**

1.  Right-click the virtual directory, and then select **Properties**.
2.  From the **Directory Security** property page, click **Edit** in the **Anonymous Access and Authentication control** group box. Disable **Anonymous Access**.
3.  Configure the virtual directory to support **Basic authentication** and **Integrated Windows authentication**.

    > [!Note]  
    > Enable SSL if you select Basic authentication. This prevents transmitting passwords in plaintext.

     

4.  From the **Virtual Directory** property page, select **Configuration**.
5.  From the **Mappings** tab of the **Application Configuration** dialog box, select **Add**. Set the **Executable** to C:\\dsfw\\bin\\adssoap.dll (or the path to adssoap.dll where it was copied). Set the **Extension** to **.dsmlx**, and then set the **Verbs** to **Limit To: POST**.
6.  This step is optional. From the **Virtual Directory** property page, set the **Application Protection** to **High** or **Medium** isolation.

## Modify the DSML configuration file

The DSML configuration file is modified to contain the Active Directory and DSML virtual directory information.

**To modify the DSML configuration file**

1.  Modify the Dsmlv2.config configuration file found in the %SystemRoot%\\system32 directory.

    The following is a generic template for the configuration file.

    ``` syntax
    <extensionConfiguration>
    <virtualDirectory url="virtualDirURL">
      <server>serverName</server>
      <port>portNumber</port>
      <useSSL>enableSSL</useSSL>
      <useSigning>enableLDAPSigning</useSigning>
      <useSealing>enableLDAPSealing</useSealing>
      <readonly>enableReadOnlyMode</readOnly>
      <connectTimeout>connTime</connectTimeout>
      <operationTimeout>operTime</operationTimeout>
      <maxConnections>numberOfConnections</maxConnections>
      <maxRequestsPerBatch>maxReqsPerBatch</maxRequestsPerBatch>
      <chaseReferrals>chaseReferralsType</chaseReferrals>
      <sessionsMax>totalSessions</sessionsMax>
      <sessionsMaxPerIP>sessionPerIP</sessionsMaxPerIP>
      <sessionsIPMatch>useIPMatching</sessionsIPMatch>
      <sessionsAuthMatch>useCredentialMatching</sessionsAuthMatch>
      <sessionsTTL>timeToLive</sessionsTTL>
      </virtualDirectory>
    </extensionConfiguration>
    ```

2.  Fill **virtualDirURL** with the URL to the extension, without the web server name. For example, if you create an IIS virtual directory named **dsml**, which allows the extension to be accessed as http://mywebserver.microsoft.com/dsml/adssoap.dsmlx, set virtualDirURL as */dsml/adssoap.dsmlx*.

    A list of virtualDirectory elements are listed on the [DSML Configuration File Elements](dsml-configuration-file-elements.md) topic.

    When configuring DSML Services for Windows manually, the following Dsmlv2.config would specify that the IIS virtual directory should process requests for an Active Directory server named testdc-01.fabrikam.com. It should connect on port 389, with connection and operation timeouts of 30 seconds. It should keep up to 10 connections open simultaneously.

    ``` syntax
    <extensionConfiguration>
       <virtualDirectory url="/dsml/adssoap.dsmlx">
            <server>testdc-01.fabrikam.com</server>
            <port>389</port>
            <connectTimeout>30</connectTimeout>
            <operationTimeout>30</operationTimeout>
            <maxConnections>10</maxConnections>
       </virtualDirectory>
    </extensionConfiguration>
    ```

    It is possible to create multiple IIS virtual directories on the web server that use the adssoap.dsmlx extension. This can be used, for example, for sending requests to different Active Directory servers. All virtual directories on an IIS server share the same Dsmlv2.config file. The IIS virtual directories must be created and configured with the proper permissions, using the steps outlined, before the DSML Services for Windows configuration file is modified.

3.  To configure a multiple virtual directory installation, create a separate virtualDirectory section for each virtual directory in the configuration file.

    For example, if you want to extend the example on [DSML Configuration File Elements](dsml-configuration-file-elements.md) to include a second virtual directory named **dsml2** that sends LDAP operations to an Active Directory server named testdc-02.fabrikam.com (also on port 389, but with no connect or operation timeout, and using the default number of connections), you could create a Dsmlv2.config file similar to the following.

    ``` syntax
    <extensionConfiguration>
       <virtualDirectory url="/dsml/adssoap.dsmlx">
            <server>testdc-01.fabrikam.com</server>
            <port>389</port>
            <connectTimeout>30</connectTimeout>
            <operationTimeout>30</operationTimeout>
            <maxConnections>10</maxConnections>
       </virtualDirectory>
    <virtualDirectory url="/dsml2/adssoap.dsmlx">
       <server>testdc-02.fabrikam.com</server>
       </virtualDirectory>
    </extensionConfiguration>
    ```

    The Dsmlv2.config file should have its file access permissions set so that all authenticated users have read access, and only administrators and IIS administrators have read/write access. This enables the DSML Services for Windows to read the configuration file while impersonating a user, yet prevents the configuration file from being subject to either accidental or malicious changes.

## Test the DSML Configuration

The DSML Services for Windows installation is now configured and ready to use.

**To test the DSML configuration**

1.  Adjust the value of the **dn** in the Search.xml file to match the Active Directory domain name.
2.  If testing a multiple virtual directory installation and the name of the virtual directory is something other than **dsml**, edit the dsmltest.vbs test script accordingly. Comments in the script file will state where the appropriate changes must occur.
3.  Run the following test script at a command prompt, using a user account that has the proper credentials to access the DSML Services for Windows Server 2003.

    **cscript dsmltest.vbs** *dsmlServerName*

The following VBScript example code demonstrates a test of the configuration.


```VB
 C:\DSfW>type search.xml

<se:Envelope xmlns:se="http://schemas.xmlsoap.org/soap/envelope/">
  <se:Body xmlns="urn:oasis:names:tc:DSML:2:0:core">
     <batchRequest>
         <searchRequest dn="dc=fabrikam,dc=com"
               scope="baseObject"
               derefAliases="neverDerefAliases"
               sizeLimit="100">
               <filter>
                   <present name="objectClass"/>
               </filter>
               <attributes>
                     <attribute name="dc"/>
                     <attribute name="description"/>
               </attributes>
         </searchRequest>
     </batchRequest>
  </se:Body>
</se:Envelope>

C:\Program Files\Microsoft\Microsoft DSMLv2 Server>cscript dsmltest.vbs dsml01

Microsoft (R) Windows Script Host Version 5.6
Copyright (C) Microsoft Corporation 1996-2001. All rights reserved.

Connecting to DSMLv2 Server...

Constructing DSML/SOAP payloads...

Sending the request...

-------RESPONSE --------
 
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" 
   xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"   
   xmlns:xsd="http://www.w3.org/2001/XMLSchema" 
  xmlns:soapenc="http://schemas.xmlsoap.org/soap/encoding/">
<soap:Body>
  <batchResponse xmlns="urn:oasis:names:tc:DSML:2:0:core" 
    xmlns:xsd="http://www.w3.org/2001/XMLSchema" 
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <searchResponse>
           <searchResultEntry dn="dc=fabrikam,dc=com">
               <attr name="dc"><value>fabrikam</value></attr>
           </searchResultEntry>
          <searchResultDone>
                 <resultCode code="0" descr="success"/>
          </searchResultDone>
   </searchResponse>
</batchResponse></soap:Body></soap:Envelope>
```



 

 




