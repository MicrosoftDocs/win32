---
description: "Learn more about: Setting the default DPI awareness for a process"
title: 'Setting the default DPI awareness for a process (Windows)'
TOCTitle: Setting the default DPI awareness for a process
ms:assetid: C9488338-D863-45DF-B5CB-7ED9B869A5E2
ms:mtpsurl: https://msdn.microsoft.com/library/Mt846517(v=VS.85)
ms:contentKeyID: 74520139
ms.date: 03/30/2018
ms.topic: article
mtps_version: v=VS.85
---

# Setting the default DPI awareness for a process

Desktop applications on Windows can run in different DPI awareness modes. These modes enable different DPI scaling behavior and can use different coordinate spaces. For more information on DPI awareness, see [High DPI Desktop Application Development on Windows.](https://msdn.microsoft.com/library/mt843498\(v=vs.85\)) It is important that you explicitly set the default DPI awareness mode of your process so as to avoid unexpected behavior.

There are two main methods to specify the default DPI awareness of a process:

1\) through an application manifest setting

2\) programmatically through an API call

We recommended that you specify the default process DPI awareness via a manifest setting. While specifying the default via API is supported, it is not recommended.

## Setting default awareness with the application manifest

There are two manifest settings that enable you to specify the process default DPI awareness mode: \<dpiAwareness\> and \<dpiAware\>. \<dpiAware\> was introduced in Windows Vista and only enables your process default to be set to system awareness. \<dpiAwareness\> was introduced in Windows 10, version 1607 and enables you to specify an ordered list of process-default DPI awareness modes. This enables you to set backup DPI awareness modes, which will be used if your application is ran on a version of Windows unable to support the first awareness mode specified. On older versions of Windows, the newer \<dpiAwareness\> tag will be ignored. This means that you can use both of these manifest settings to enable a scenario where your process default could be system awareness on older version of Windows while being Per-Monitor on versions greater than Windows 10, version 1607. On Windows 10, version 1607, and on, the \<dpiAware\> setting is ignored if the \<dpiAwareness\> element is present.

The table below shows how to specify different process-default DPI awareness modes using the two manifest settings:

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th>Process default DPI awareness mode</th>
<th>&lt;dpiAware&gt; setting</th>
<th>&lt;dpiAwareness&gt; setting (Windows 10, version 1607 and later)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>unaware</td>
<td><p>N/A (no dpiAware setting in manifest)</p>
<p>or</p>
<p>&lt;dpiAware&gt;false&lt;/dpiAware&gt;</p></td>
<td>&lt;dpiAwareness&gt;unaware&lt;/dpiAwareness&gt;</td>
</tr>
<tr class="even">
<td>System aware</td>
<td>&lt;dpiAware&gt;true&lt;/dpiAware&gt;</td>
<td>&lt;dpiAwareness&gt;system&lt;/dpiAwareness&gt;</td>
</tr>
<tr class="odd">
<td>Per Monitor</td>
<td>&lt;dpiAware&gt;true/pm&lt;dpiAware&gt;</td>
<td>&lt;dpiAwareness&gt;PerMonitor&lt;/dpiAwareness&gt;</td>
</tr>
<tr class="even">
<td>Per Monitor V2</td>
<td>Not supported</td>
<td>&lt;dpiAwareness&gt;PerMonitorV2&lt;/dpiAwareness&gt;</td>
</tr>
</tbody>
</table>

 

The sample below shows both the \<dpiAwareness\> and the \<dpiAware\> settings being used within the same manifest file to configure process-default DPI awareness behavior for different versions of Windows.

```xml
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<assembly xmlns="urn:schemas-microsoft-com:asm.v1" manifestVersion="1.0" xmlns:asmv3="urn:schemas-microsoft-com:asm.v3">
  <asmv3:application>
    <asmv3:windowsSettings>
      <dpiAware xmlns="http://schemas.microsoft.com/SMI/2005/WindowsSettings">true</dpiAware>
      <dpiAwareness xmlns="http://schemas.microsoft.com/SMI/2016/WindowsSettings">PerMonitorV2</dpiAwareness>
    </asmv3:windowsSettings>
  </asmv3:application>
</assembly>
```

## Setting default awareness programmatically

Although it is not recommended, it is possible to set the default DPI awareness programmatically. Once a window (an HWND) has been created in your process, changing the DPI awareness mode is no longer supported. If you are setting the process-default DPI awareness mode programmatically, you must call the corresponding API before any HWNDs have been created.

There are multiple APIs that let you specify the default DPI awareness for your process. The current recommended API is [**SetProcessDpiAwarenessContext**](https://msdn.microsoft.com/library/mt807676\(v=vs.85\)), as older APIs offer less functionality.

 

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr class="header">
<th>API</th>
<th>Minimum version of Windows</th>
<th>DPI Unaware</th>
<th>System DPI Aware</th>
<th>Per Monitor DPI Aware</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><a href="/windows/win32/api/winuser/nf-winuser-setprocessdpiaware">SetProcessDpiAware</a></td>
<td>Windows Vista</td>
<td>N/A</td>
<td>SetProcessDpiAware()</td>
<td>N/A</td>
</tr>
<tr class="even">
<td><a href="/windows/win32/api/shellscalingapi/nf-shellscalingapi-setprocessdpiawareness"><strong>SetProcessDpiAwareness</strong></a></td>
<td>Windows 8.1</td>
<td>SetProcessDpiAwareness(PROCESS_DPI_UNAWARE)</td>
<td>SetProcessDpiAwareness(PROCESS_DPI_SYSTEM_DPI_AWARE)</td>
<td>SetProcessDpiAwareness(PROCESS_DPI_PER_MONITOR_DPI_AWARE)</td>
</tr>
<tr class="odd">
<td><a href="/windows/win32/api/winuser/nf-winuser-setprocessdpiawarenesscontext"><strong>SetProcessDpiAwarenessContext</strong></a></td>
<td>Windows 10, version 1607</td>
<td>SetProcessDpiAwarenessContext(DPI_AWARENESS_CONTEXT_UNAWARE)</td>
<td>SetProcessDpiAwarenessContext(DPI_AWARENESS_CONTEXT_SYSTEM_AWARE)</td>
<td><p>SetProcessDpiAwarenessContext(DPI_AWARENESS_CONTEXT_PER_MONITOR_AWARE)</p>
<p>SetProcessDpiAwarenessContext(DPI_AWARENESS_CONTEXT_PER_MONITOR_AWARE_V2)</p></td>
</tr>
</tbody>
</table>

 

## Process-default vs. Thread default

This document refers to setting the default DPI awareness for your process. This is because Windows 10 introduced support for running more than one DPI awareness mode within a single process (prior to Windows 10, the entire process had to conform to a single DPI awareness mode). Support for running more than one DPI awareness mode within a process is referred to as "mixed-mode DPI scaling". When using mixed-mode DPI scaling within your process, each top-level Window can run in a DPI awareness mode that may be different than that of the process default. Unless explicitly specified, each thread will default to the process default when created. For more information about mixed-mode DPI scaling, refer to the [Mixed-Mode DPI Scaling](https://msdn.microsoft.com/library/mt744321\(v=vs.85\)) article.
