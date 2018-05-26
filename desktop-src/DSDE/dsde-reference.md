---
Description: Directory Services Data Exchange (DSDE) is a command-prompt utility. It processes input from either the command line or a DSML request document file. It returns results to the command prompt window or the specified output file.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 580cb260-277b-4574-acbc-18069477e2d6
ms.prod: windows-server-dev
ms.technology: active-directory-domain-services
ms.tgt_platform: multiple
title: DSDE Reference
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# DSDE Reference

Directory Services Data Exchange (DSDE) is a command-prompt utility. It processes input from either the command line or a DSML request document file. It returns results to the command prompt window or the specified output file.

The DSDE command line syntax is as follows:

``` syntax
dsde [flag1 [flag2 ...]
```

The **/mode** flag is required. If **/mode IMPORT** is specified, then the **/input** flag is also required. All other command line flags are optional. If no flags are specified, then DSDE will output the online help to the command prompt window.

The DSDE command line flags are categorized as follows. Flags that are not exclusively export or import specific can be used in either import or export mode.

-   [General Arguments](#general-arguments)
-   [Export-Specific Arguments](#export-specific-arguments)
-   [Import-Specific Arguments](#import-specific-arguments)
-   [Credential-Handling Arguments](#credential-handling-arguments)

## General Arguments

The following table lists general arguments that can be used in import and export modes.



| Flag                                            | Abbr.                | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|-------------------------------------------------|----------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **/server ***Name*<br/>                   | **/srv**<br/>  | Specifies the name or virtual directory of the server. It can be a DC, a domain name, or the complete URL address of a DSML Services for Windows ISAPI Extension module (adssoap.dsmlx). The default is the current Active Directory domain controller.<br/>                                                                                                                                                                                                                                                                                              |
| **/port ***Number*<br/>                   | **/p**<br/>    | Specifies the port number that is used to connect to the server. The default is 389 for LDAP, 636 for LDAP using SSL, 80 for DSML, and 443 for DSML using SSL.<br/>                                                                                                                                                                                                                                                                                                                                                                                       |
| **/protocol **\[**LDAP**\|**DSML**\]<br/> | **/prot**<br/> | Specifies the protocol format used to communicate with the server. The default is LDAP.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| **/opTimeout ***Seconds*<br/>             | **/ot**<br/>   | Specifies the timeout, in seconds, for each DSDE operation.<br/> The overall command timeout is computed by DSDE. The total timeout value is the number of individual operations times the specified timeout value.<br/> The default is 120.<br/>                                                                                                                                                                                                                                                                                             |
| **/conTimeout ***Seconds*<br/>            | **/ct**<br/>   | Specifies the timeout, in seconds, for the initial connection.<br/> The connection timeout is measured from the point that the initial request sent to the server until the point the server responds to the client for establishing a connection.<br/> The default is 300.<br/>                                                                                                                                                                                                                                                              |
| **/output ***FileSpec*<br/>               | **/out**<br/>  | Specifies the name of the output file for the results. This is normally used in the Export mode. If used in import mode, it writes the server command responses to the specified file.<br/> If **/output** is omitted, the results can also be redirected to a file with the use of the standard command line redirection operators; that is **&gt;** or **&gt;&gt;**.<br/> The output is written to the command prompt window (standard console) in export mode. By default, Server command response output is disabled in import mode.<br/> |
| **/quiet**<br/>                           | **/q**<br/>    | Specifies **quiet** mode. The **quiet** mode eliminates most of the extra status messages sent to the standard output. By default, both the Import and Export modes are in **verbose** mode.<br/>                                                                                                                                                                                                                                                                                                                                                         |
| **/logDirectory ***DirSpec*<br/>          | **/log**<br/>  | Specifies the name of the log file directory and enables the creation of the dsde.log log file. If omitted, no log file is created.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                  |
| **/mode **\[**IMPORT**\|**EXPORT**\]<br/> | **/m**<br/>    | Specifies the mode in which DSDE runs. The default is **EXPORT**.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| **/ssl**<br/>                             |                      | Enables SSL encryption for all communications with the server. By default, SSL is not enabled.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| **/encrypt**<br/>                         | **/enc**<br/>  | Enables SASL-layer data encryption for communications with the server. It is only supported when using the LDAP protocol. It cannot be used simultaneously with the **/ssl** option.<br/> By default, SASL-layer encryption is not enabled.<br/>                                                                                                                                                                                                                                                                                                    |
| **/replace ***FromDN*** ***ToDN*<br/>     | **/repl**<br/> | Replaces all occurrences of *fromDN* with *toDN*. These replacements are performed on the DNs and the attribute values of the objects.<br/>                                                                                                                                                                                                                                                                                                                                                                                                               |
| **/referral **\[**ON**\|**OFF**\]<br/>    | **/rf**<br/>   | Enables or disables referral chasing when a referral is generated by the server. Referral chasing is restricted to the LDAP protocol.<br/> The default is **OFF**.<br/>                                                                                                                                                                                                                                                                                                                                                                             |
| **/?**<br/>                               |                      | Outputs online help to the standard console.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |



 

## Export-Specific Arguments

The following table lists arguments that can be used only in export mode.



| Flag                                                           | Abbr.                 | Description                                                                                                                                                                                                                                                                                                                                                                                                             |
|----------------------------------------------------------------|-----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **/query ***Filter*<br/>                                 | **/qS**<br/>    | Specifies a command line LDAP query. The default is (objectClass=\*).<br/>                                                                                                                                                                                                                                                                                                                                        |
| **/baseDN ***DN*<br/>                                    | **/dn**<br/>    | Specifies the root of the LDAP search.<br/>                                                                                                                                                                                                                                                                                                                                                                       |
| **/scope ** \[**BASE**\|**ONELEVEL**\|**SUBTREE**\]<br/> | **/sc**<br/>    | Specifies the scope of the LDAP query. The default is **SUBTREE**.<br/>                                                                                                                                                                                                                                                                                                                                           |
| **/attributes ***AttrList*<br/>                          | **/attr**<br/>  | Specifies a comma-delimited list of attributes that will be returned in the results set. The list must be entered without extraneous spaces, so any attribute names with embedded spaces must be enclosed inside double-quotes.<br/> This flag cannot be used with the **/excludedAttributes** flag.<br/> By default, all attributes are returned.<br/>                                               |
| **/excludedAttributes ***AttrList*<br/>                  | **/Xattr**<br/> | Specifies a comma-delimited list of attributes that will be excluded in the results set; all other attributes not in the list will be returned. The list must be entered without extraneous spaces, so any attribute names with embedded spaces must be enclosed inside double-quotes.<br/> This flag cannot be used with the **/attributes** flag.<br/> By default, no attributes are excluded.<br/> |
| **/pageSize ***Count*<br/>                               | **/page**<br/>  | Specifies the page size used for search operations. If set to **0**, paging is disabled. The default is 100.<br/>                                                                                                                                                                                                                                                                                                 |
| **/outRequest**<br/>                                     | **/Oreq**<br/>  | Transforms all **searchResponse** results to request operations before returning the results to the user. This flag is valid only if the mode is set to **EXPORT**.<br/> The result of this flag is to format the results of the DSDE operation into a format that can be used as an input request document.<br/> By default, no transformation is performed.<br/>                                    |



 

## Import-Specific Arguments

The following table lists arguments that can be used only in import mode.



| Flag                                     | Abbr.                | Description                                                                                                                                                                                                                                                                       |
|------------------------------------------|----------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **/input ***FileSpec*<br/>         | **/in**<br/>   | Specifies the name of the input file for the request document.<br/>                                                                                                                                                                                                         |
| **/resume**<br/>                   | **/rm**<br/>   | Specifies that the server should resume with the next input operation when an error occurs.<br/> This flag overrides any **onError="exit"** command in the DSML v2 input request file.<br/> By default, error resume is disabled.<br/>                          |
| **/bulk **\[**ON**\|**OFF**\]<br/> | **/bk**<br/>   | Enables or disables the LazyCommit behavior of the server. LazyCommit causes the server to return the response to a modification command after it has completed in the server's memory but before it has been committed to disk by the server. The default is **ON**.<br/>  |
| **/requestsPerBatch**<br/>         | **/reqs**<br/> | This option can be used only when using the DSML protocol. When using the DSML protocol, DSDE batches together multiple import operations into one batchRequest. This option specifies the maximum number of operations to include in each batch. The default is 1000.<br/> |



 

## Credential-Handling Arguments

The following table lists credential-handling arguments, which can be used in import and export modes.



| Flag                                                             | Abbr.                | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|------------------------------------------------------------------|----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **/cred ***UserName*** ***Password*<br/>                   | **/cr**<br/>   | Specifies alternate user credentials. If an asterisk (**\***) is specified for the password argument, the user will be prompted for a password by the command prompt window. The prompted password is not echoed to the command windows. The default is the credentials for the current user.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| **/authFlag ** \[**NEGO**\|**BASIC**\|**ANONYMOUS**\]<br/> | **/auth**<br/> | Specifies the authentication method used between the client and server computers. The default is **NEGO**.<br/> **NEGO** Negotiate. Credentials are not required, and if not specified the credentials default to the current logon user. If authenticating against a DSML Services for Windows server, IIS Windows Integrated Authentication is used.<br/> **BASIC** Credentials are required. If authenticating against a DSML Services for Windows server, an HTTP Basic Authentication is performed. If authenticating against an LDAP server, an LDAP simple bind is performed.<br/> **BASIC** authentication for either LDAP or DSML Services for Window always transmits the *UserName* and *Password* credentials as plaintext across the network, unless SSL is used to encrypted the underlying network traffic.<br/> **ANONYMOUS** Credentials are not allowed. If authenticating against a DSML Services for Windows server, the IIS Anonymous user account is used. If authenticating against an LDAP server, an anonymous LDAP bind is performed.<br/> |



 

## Remarks

While DSDE runs, DSDE will echo processing status messages to the command prompt window (standard output) as a way to provide user feedback. Specifying **/quiet** disables the user feedback output.

The following events will generate echo:

-   DSDE receives **errorResponse**.
-   DSDE completes the process. If no **errorResponse**and LDAP Error are reported, it should report as **Command completed successfully**. If there are one or more errors, DSDE should report as **Command completed with error(s)**.

### Character Sets Used in DSDE

DSDE will always produce Unicode files, including all export and log files.

DSDE will probe any input file if the character set is not specified. If the input file appears to be Unicode, then it will be processed as all Unicode. If the input file appears to be ANSI, then it will be processed as all ANSI.

### DSDE Referral Chasing Behavior

In the current release, there are three scenarios where chase Referral is applicable:

-   Protocol is set to DSML and the DSML Services for Windows server produces an HTTP REF URL to DSDE.
-   Protocol is set to DSML and the DSML Services for Windows server returns an LDAP Referral to DSDE.
-   The protocol is set to LDAP and the LDAP directory server returns an LDAP referral to DSDE.

DSDE will chase the referral only if the chase referral switch is turned on and the directory server returns an LDAP referral to DSDE. In all other cases DSDE will ignore the referral.

## Examples

The following examples show DSDE command prompt usage.

The first example performs an export of all objects under the default naming context using the LDAP protocol. DSDE outputs the search results to the console, which is then redirected to a file named "dit.xml"

**DSDE /qS (objectClass=\*) &gt; dit.xml**

The second example performs an import of the contents of the file "import.xml". It uses the DSML protocol to talk to a server named "myServer" by specifying the complete URL of the server's DSML ISAPI extension module.

**DSDE /in import.xml /protocol dsml /server http://myServer/dsml/adssoap.dsmlx /m import**

The third example performs an export using the DSML protocol. It exports all objects with an **objectClass** of user and an **objectCategory** of person located under the default naming context and stores the results in a file named "user.xml".

**DSDE /query (&(objectClass=user)(objectCategory=person)) /prot dsml /server http://myServer/dsml/adssoap.dsmlx /out user.xml**

 

 




