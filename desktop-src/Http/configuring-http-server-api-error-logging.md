---
title: Configuring HTTP Server API Error Logging
description: The HTTP Server API error logging is controlled by three registry values under an HTTP\\Parameters key.
ms.assetid: a7712159-939e-42e3-a8d8-73148c2f4f6e
keywords:
- HTTP Server API, configuring error logs
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Configuring HTTP Server API Error Logging

The HTTP Server API error logging is controlled by three registry values under an **HTTP**\\**Parameters** key located at:

```
HKEY_LOCAL_MACHINE
   System
      CurrentControlSet
         Services
            HTTP
               Parameters
```

> [!Note]  
> The location and form of the configuration values may change in future versions of the Windows operating system.

 

A user must have Administrator/Local System privileges to modify the registry values, and view or modify the log files and the folder that contains them.

Configuration information in the registry values is read when the HTTP Server API driver is started. As a result, if the settings are changed the driver must be stopped and restarted to read the new values. This can be accomplished by using the following console commands:

**net stop http**

**net start http**

The log files are named by using the following convention:

**httperr +** *SequenceNumber* **+ .log**

For example: "httperr4.log".

Log files are cycled when they reach the maximum size specified by the **ErrorLogFileTruncateSize** registry value, and the value cannot be less than one megabyte (MB).

If the configuration of error logging is invalid or any kind of failure occurs while writing to the log files, the HTTP Server API uses event logging to notify administrators that error logging did not take place.

Registry configuration values are described in the following table.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Registry Value</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><span id="EnableErrorLogging"></span><span id="enableerrorlogging"></span><span id="ENABLEERRORLOGGING"></span>EnableErrorLogging<br/></td>
<td>A <strong>DWORD</strong> that can be set to <strong>TRUE</strong> to enable error logging, or <strong>FALSE</strong> to disable it. The default value is <strong>TRUE</strong>.<br/></td>
</tr>
<tr class="even">
<td><span id="ErrorLogFileTruncateSize"></span><span id="errorlogfiletruncatesize"></span><span id="ERRORLOGFILETRUNCATESIZE"></span>ErrorLogFileTruncateSize<br/></td>
<td>A <strong>DWORD</strong> that specifies the maximum size of an error log file, in bytes. The default value is one MB (0x100000).<br/>
<blockquote>
[!Note]<br />
The specified value cannot be smaller than the default value.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td><span id="ErrorLoggingDir"></span><span id="errorloggingdir"></span><span id="ERRORLOGGINGDIR"></span>ErrorLoggingDir<br/></td>
<td>A <strong>String</strong> that specifies the folder under which the HTTP Server API places its logging files. <br/> The HTTP Server API creates a subfolder named &quot;HTTPERR&quot; under the specified folder into which the log files are placed. This subfolder and the log files receive the same permission settings, which means that Administrator and Local System Accounts have full access, while other users do not have access.<br/> If a folder is not specified in the registry, the default folder is the following:<br/> &quot;%SystemRoot%\System32\LogFiles&quot;<br/>
<blockquote>
[!Note]<br />
The ErrorLoggingDir string value must be a fully qualified path, but it can contain &quot;%SystemRoot%&quot;.
</blockquote>
<br/> <br/></td>
</tr>
</tbody>
</table>



 

 

 





