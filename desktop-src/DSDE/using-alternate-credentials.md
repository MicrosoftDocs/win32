---
Description: 'This example uses DSDE to export employee data to a file from the fabrikam.com Active Directory. It performs the same search as the Exporting Active Directory Objects example, but specifies a set of alternate security credentials.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\mbaldwin'
ms.assetid: 'fc662cf1-cdca-4a22-9863-28619dd14fa1'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-domain-services'
ms.tgt_platform: multiple
title: Using Alternate Credentials
---

# Using Alternate Credentials

This example uses DSDE to export employee data to a file from the fabrikam.com Active Directory. It performs the same search as the [Exporting Active Directory Objects](exporting-active-directory-objects.md) example, but specifies a set of alternate security credentials.

The following code example runs from a command line. To open a command prompt window, click **Start** on the taskbar and then click **Command Prompt**.

``` syntax
C:\Documents and Settings\MyUserName> cd \program files\microsoft\dsde
C:\Program Files\Microsoft\DSDE> dsde /mode export 
                                      /baseDN CN=Users,DC=fabrikam,DC=com 
                                      /scope oneLevel 
                                      /protocol LDAP 
                                      /output employees.xml 
                                      /attributes name,sn,givenName,title,telephoneNumber,objectClass
                                      /cred jeffsmith sec#re8Tt~!
```

> [!Note]  
> For clarity, the command line is shown divided into several lines. Normally, it will be entered all on one line.

 

The command line options used in this example perform the following functions:

-   The **/mode export** option causes DSDE to operate in export mode. This retrieves objects from the directory.
-   The **/baseDN** option specifies where the search base begins when retrieving directory objects. Because this example did not specify a search filter with the **/query** option, the search defaults to all objects: (objectClass=\*).
-   The **/scope** option specifies the search scope. It could be *base*, *oneLevel*, or *subTree*.
-   The **/protocol** option specifies the protocol DSDE uses to communicate with the server. LDAP is used in this example.
-   The **/output** option specifies the file name to be created as an output file. DSDE uses DSML V2 format for the output file.
-   The **/attributes** option specifies the attributes to be retrieved. If none are specified, DSDE retrieves all attributes.
-   The **/cred** option specifies alternate credentials from the currently logged on user.

When using alternate credentials, use the **/cred** option followed by the user name and password. Using an asterisk (\*) as the password on the command line will cause DSDE to prompt the user for the password. As you type the password, DSDE will not echo it to the console.

The following is a partial list of the resulting Employees.xml output file.

``` syntax
<batchResponse xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
               xmlns:xsd="http://www.w3.org/2001/XMLSchema" 
               xmlns="urn:oasis:names:tc:DSML:2:0:core">
  <searchResponse>
    <searchResultEntry dn="CN=Administrator,CN=Users,DC=fabrikam,DC=com">
      <attr name="objectClass">
        <value>top</value>
        <value>person</value>
        <value>organizationalPerson</value>
        <value>user</value>
      </attr>
      <attr name="name">
        <value>Administrator</value>
      </attr>
    </searchResultEntry>
    ...  
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
    ...
    <searchResultDone>
      <resultCode code="0" descr="success"/>
    </searchResultDone>
  </searchResponse>
</batchResponse>
```

 

 



