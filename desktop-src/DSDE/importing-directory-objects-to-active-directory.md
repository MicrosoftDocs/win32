---
Description: 'This example uses DSDE to import employee data to the fabrikam.com Active Directory.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\mbaldwin'
ms.assetid: '4b6a1646-3943-4da9-8ab7-5e8eab57086a'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-domain-services'
ms.tgt_platform: multiple
title: Importing Directory Objects to Active Directory
---

# Importing Directory Objects to Active Directory

This example uses DSDE to import employee data to the fabrikam.com Active Directory.

The following example runs from a command line. To open a command prompt window, click **Start** on the taskbar and then click **Command Prompt**.

``` syntax
C:\Documents and Settings\MyUserName> cd \program files\microsoft\dsde
C:\Program Files\Microsoft\DSDE> dsde /mode import 
                                      /input employees.xml
                                      /server fabricam.com
                                      /protocol LDAP 
                                      /resume
```

> [!Note]  
> For clarity, the command line is shown divided into several lines. Normally, it would be entered all on one line.

 

The command line options used in this example perform the following functions:

-   The **/mode import** option causes DSDE to operate in import mode. This adds or modifies objects in the directory.
-   The **/input** option specifies the file name to be used as the input file, which must be a valid DSML V2 document. The import mode always requires that the **/input** option be specified.
-   The **/server** option specifies the name of the directory server to connect to.
-   The **/protocol** option specifies the protocol that DSDE uses to communicate with the server. LDAP is used in this example.
-   The **/resume** option allows DSDE to continue operation even if an error occurs in processing the input file commands.

    > [!Note]  
    > In the case of catastrophic errors, such as network outages or server malfunctions, DSDE cannot honor the **/resume** request.

     

 

 



