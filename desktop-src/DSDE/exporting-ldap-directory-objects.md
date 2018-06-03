---
Description: This example uses DSDE to export employee data from one LDAP directory to a file. It reformats the data so that it can be imported to the fabrikam.com Active Directory.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 79532ce9-f0c7-4e65-9655-b0081e39525f
ms.prod: windows-server-dev
ms.technology: active-directory-domain-services
ms.tgt_platform: multiple
title: Exporting LDAP Directory Objects
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Exporting LDAP Directory Objects

This example uses DSDE to export employee data from one LDAP directory to a file. It reformats the data so that it can be imported to the fabrikam.com Active Directory.

This example runs from a command line. To open a command prompt window, click **Start** on the taskbar and then click **Command Prompt**.

``` syntax
C:\Documents and Settings\MyUserName> cd \program files\microsoft\dsde
C:\Program Files\Microsoft\DSDE> dsde /mode export 
                                      /query (sn=Smith)
                                      /baseDN OU=myProject,O=myCompany
                                      /scope oneLevel 
                                      /server localhost 
                                      /protocol LDAP 
                                      /port 1026
                                      /output employees.xml
                                      /replace OU=myProject,O=myCompany CN=Users,DC=fabrikam,DC=com
                                      /outRequest
                                      /attributes name,sn,givenName,title,telephoneNumber,objectClass
```

> [!Note]  
> For clarity, the command line is shown divided into several lines. Normally, it would be entered all on one line.

 

The command line options used in this example perform the following functions:

-   The **/mode export** option causes DSDE to operate in export mode. This retrieves objects from the directory.
-   The **/query** option passes an LDAP search filter string to the directory server. This example searches for all User objects with a surname equal to *Smith*.
-   The **/baseDN** option specifies where the search base begins when retrieving directory objects.
-   The **/scope** option specifies the search scope. It could be *base*, *oneLevel*, or *subTree*.
-   The **/server** option specifies the name of the directory server to connect to.
-   The **/protocol** option specifies the protocol that DSDE uses to communicate with the server. LDAP is used in this example.
-   The **/port** option specifies a specific port number used to connect to the directory server. The default port number is 389.
-   The **/output** option specifies the file name to be created as an output file. DSDE uses DSML V2 format for the output file.
-   The **/replace** option causes DSDE to replace any occurrence of the first string with the second in the Distinguished Name attribute. In this example, any **searchResultEntry** returned that contains "**OU=myProject,O=myCompany**" as part of the **dn** attribute will have that part of the **dn** attribute replaced with "**CN=Users,DC=fabrikam,DC=com**".
-   The **/outRequest** option causes DSDE to convert each **searchResultEntry** returned into a corresponding **addRequest** operation. This allows the output results file to be used as an import file in a subsequent call to DSDE.

    > [!Note]  
    > The **/outRequest** option does not guarantee the order of the resulting **addRequest** operations. DSDE does not guarantee that the **addRequest** for parent objects will appear before any child object.

     

-   The **/attributes** option specifies the attributes to be retrieved. If none are specified, DSDE retrieves all attributes.

The following is a partial listing of the resulting employees.xml output file.

``` syntax
<batchRequest xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
              xmlns:xsd="http://www.w3.org/2001/XMLSchema" 
              xmlns="urn:oasis:names:tc:DSML:2:0:core">
  <addRequest dn="CN=Jeff Smith,CN=Users,DC=fabrikam,DC=com">
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
      <value>(425) 555-0174</value>
    </attr>               
    <attr name="givenName">
      <value>Jeff</value>
    </attr>
    <attr name="name">
      <value>Jeff Smith</value>
    </attr>
  </addRequest>
  <addRequest dn="CN=Jeff Smith,CN=Users,DC=fabrikam,DC=com">
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
      <value>Program Manager</value>
    </attr>
    <attr name="telephoneNumber">
      <value>(425) 707-9798</value>
    </attr>               
    <attr name="givenName">
      <value>Jeff</value>
    </attr>
    <attr name="name">
      <value>Jeff Smith</value>
    </attr>
  </addRequest>
</batchRequest>
```

 

 



