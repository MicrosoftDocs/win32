---
Description: 'This example uses DSDE to export employee data to a file from the fabrikam.com Active Directory using DSML Services for Windows.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\mbaldwin'
ms.assetid: '28b99b66-954b-4bdf-b7a0-6ffb92cdebfb'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-domain-services'
ms.tgt_platform: multiple
title: Exporting Active Directory Objects Through DSML Services for Windows
---

# Exporting Active Directory Objects Through DSML Services for Windows

This example uses DSDE to export employee data to a file from the fabrikam.com Active Directory using DSML Services for Windows.

The following example runs from a command line. To open a command prompt window, click **Start** on the taskbar and then click **Command Prompt**.

``` syntax
C:\Documents and Settings\MyUserName> cd \program files\microsoft\dsde
C:\Program Files\Microsoft\DSDE> dsde /mode export
                                      /query (sn=Smith)
                                      /baseDN CN=Users,DC=fabrikam,DC=com 
                                      /server http://www.fabrikam.com/dsml/adssoap.dsmlx
                                      /protocol DSML
                                      /output employees.xml 
                                      /attributes name,sn,givenName,title,telephoneNumber,objectClass
```

> [!Note]  
> For clarity, the command line is shown divided into several lines. Normally, it will be entered all on one line.

 

The command line options used in this example perform the following functions:

-   The **/mode export** option causes DSDE to operate in export mode. This retrieves objects from the directory.
-   The **/query** option passes an LDAP search filter string to the directory server. This example searches for all User objects with a surname equal to *Smith*.
-   The **/baseDN** option specifies where the search base begins when retrieving directory objects.
-   The **/server** option specifies the full URL location of the DSML Services for Windows ISAPI Extension module (adssoap.dsmlx).
-   The **/protocol** option specifies the protocol that DSDE uses to communicate with the server. DSML Services for Windows is used in this example.
-   The **/output** option specifies the file name to be created as an output file. DSDE uses DSML V2 format for the output file.
-   The **/attributes** option specifies the attributes to be retrieved. If none are specified, DSDE retrieves all attributes.

The following is a partial listing of the resulting employees.xml output file.

``` syntax
<batchResponse xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
               xmlns:xsd="http://www.w3.org/2001/XMLSchema" 
               xmlns="urn:oasis:names:tc:DSML:2:0:core">
  <searchResponse>
    <searchResultEntry dn="CN=Jeff Smith,CN=Users,DC=fabrikam,DC=com">
      <attr name="objectClass">
        <value>top</value>
        <value>person</value>
        <value>organizationalPerson</value>
        <value>user</value>
      </attr>
      <attr name="sn">
        <value>Smith</value>
      </attr>
      <attr name="title">
        <value>Developer</value>
      </attr>
      <attr name="telephoneNumber">
        <value>(999) 999-9999</value>
      </attr>    
      <attr name="givenName">
        <value>Jeff</value>
      </attr>
      <attr name="name">
        <value>Jeff Smith</value>
      </attr>
    </searchResultEntry>
    <searchResultDone>
      <resultCode code="0" descr="success"/>
    </searchResultDone>
  </searchResponse>
</batchResponse>
```

 

 



