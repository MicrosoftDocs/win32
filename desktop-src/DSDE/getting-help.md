---
Description: 'To diagnose problems when using DSDE, create a log file when issuing a DSDE command. The /log option is used to generate a log file.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\mbaldwin'
ms.assetid: '0efd0e60-1e8c-4c21-9d42-cbe024732463'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-domain-services'
ms.tgt_platform: multiple
title: Diagnosing Errors with a Log File
---

# Diagnosing Errors with a Log File

To diagnose problems when using DSDE, create a log file when issuing a DSDE command. The **/log** option is used to generate a log file.

The following example shows how to create a log file. This example runs from a command line. To open a command prompt window, click **Start** on the taskbar and then click **Command Prompt**.

``` syntax
C:\Documents and Settings\MyUserName> cd \program files\microsoft\dsde
C:\Program Files\Microsoft\DSDE> dsde /mode import 
                                      /input employeees.xml
                                      /server fabricam.com
                                      /protocol LDAP 
                                      /resume
                                      /log .
```

> [!Note]  
> For clarity, the command line is shown divided into several lines. Normally, it would be entered all on one line.

 

The command line options used in this example perform the following functions:

-   The **/mode import** option causes DSDE to operate in import mode. This adds or modifies objects in the directory.
-   The **/input** option specifies the file name to be used as the input file, which must be a valid DSMLV2 document. The import mode always requires that the **/input** option be specified.
-   The **/server** option specifies the name of the directory server to connect to.
-   The **/protocol** option specifies the protocol that DSDE uses to communicate with the server. LDAP is used in this example.
-   The **/resume** option allows DSDE to continue operation even if an error occurs in processing the input file commands.

    > [!Note]  
    > In the case of catastrophic errors, such as network outages or server malfunctions, DSDE cannot honor the **/resume** request.

     

-   The **/log** option causes DSDE to create a dsde.log file. The period argument specifies that the log file will be placed in the current directory.

The following is a listing of a possible dsde.log file when an error has occurred:

``` syntax
<log>
<cmd>dsde /mode import /input employeees.xml /server fabrikam.com /protocol LDAP /resume /log .</cmd>
<date>2003-01-14T13:56:22</date>
<error type="internal">Could not find file "C:\Program Files\Microsoft\DSDE\employeees.xml".</error>
<status>Command completed with error(s).</status>
</log>
```

 

 



