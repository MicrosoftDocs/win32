---
title: .Htx File Errors
description: .Htx File Errors
ms.assetid: 4c2bb15f-fcdb-4d3a-9627-dc96e2c47993
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# .Htx File Errors

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

These messages are for Internet Data Query (.idq) processing only and are returned by the *CiErrorMessage* variable, accessible from HTML extension file (.htx) error pages.



| Message                                                                                                                                          | Explanation                                                                                                                                      |
|--------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| A &lt;%BeginDetail%&gt; section was found on line &lt;number&gt; in the .htx file &lt;file&gt;, without a matching &lt;%EndDetail%&gt; section.  | The &lt;%BeginDetail%&gt; tag must be followed by a matching &lt;%EndDetail%&gt; tag.                                                            |
| An &lt;%else%&gt; or &lt;%endif%&gt; was found without a matching &lt;%if...%&gt;.                                                               | An &lt;%else%&gt; or &lt;%endif%&gt; tag was found without a matching &lt;%if %&gt; tag.                                                         |
| An &lt;%EndDetail%&gt; section was found on line &lt;number&gt; in the .htx file &lt;file&gt; before the &lt;%BeginDetail%&gt; section.          | The &lt;%BeginDetail%&gt; tag must precede the &lt;%EndDetail%&gt; tag.                                                                          |
| An &lt;%EndDetail%&gt; section was found on line &lt;number&gt; in the .htx file &lt;file&gt;, without a matching &lt;%BeginDetail%&gt; section. | The &lt;%EndDetail%&gt; tag must be preceded by a matching &lt;%BeginDetail%&gt; tag.                                                            |
| An &lt;%if%&gt; was found without a matching &lt;%else%&gt; or &lt;%endif%&gt;.                                                                  | The &lt;%if...%&gt; tag must be followed by an &lt;%endif%&gt; tag, with an optional &lt;%else%&gt; tag in between.                              |
| Constants used in IsTypeEq-operator conditions must be unsigned integers, not floats, globally unique identifiers (GUIDs), and so on.            | One or more of the constants in the IsTypeEq condition is a float, GUID, and so on, but should be an unsigned integer.                           |
| Expecting an operator in &lt;%if%&gt; statement.                                                                                                 | The operator in an &lt;%if...%&gt; tag was missing. 'If' must be followed by one of EQ, NE, LT, LE, GT, GE, contains, or IsTypeEq HTX operators. |
| The .htx file &lt;file&gt; contains an ill-formed include statement on line &lt;number&gt;.                                                      | Usually caused by a &lt;%include...%&gt; tag without the closing %&gt;.                                                                          |
| The .htx file &lt;file&gt; uses too many includes on line &lt;number&gt;.                                                                        | A maximum of 32 files can be included by use of the &lt;%include...%&gt; tag.                                                                    |
| The .htx file specified could not be found in any virtual or physical path.                                                                      | The .htx file specified in an &lt;%include...%&gt; tag could not be located.                                                                     |
| The include file name is invalid in file &lt;file&gt; on line &lt;number&gt;.                                                                    | Usually caused by a &lt;%include...%&gt; tag missing the closing %&gt;.                                                                          |
| One of the values in a IsTypeEq condition must be a variable. You used two constants.                                                            | One of the values in the IsTypeEq condition must be a variable.                                                                                  |
| An opening bracket "{" was found without a matching closing bracket.                                                                             | A vector in an &lt;%if...%&gt; tag is missing the closing brace.                                                                                 |
| An opening quotation mark (") was found without a matching closing quotation mark (").                                                           | A quoted phrase in an &lt;%if...%&gt; tag is missing the closing quote.                                                                          |



 

 

 




