---
title: How to Enable error and performance logging
description: The Rights Management SDK 4.2 manages diagnosis and performance logs upload through a single device property.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 'F5AD3826-2292-4A25-AF5C-D17D083F5742'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
---

# How to: Enable error and performance logging

The Rights Management SDK 4.2 manages diagnosis and performance logs upload through a single device property.

## Overview

You can improve your users' experience and troubleshooting by enabling automatic diagnostics and performance logging upload to Microsoft. In order to honor user privacy, you as the app developer, must ask the user to consent before enabling the automatic logging.

You will manager logging control through two properties.

-   Enable logging through the **IpcCustomerExperienceDataCollectionEnabled** property. The setting is persistent across device resets.
-   Control the logging level through the **IpcLogLevel** property using the following settings. <dl> 1 - Verbose  
    2 - Informational  
    3 - Warning  
    4 - Error  
    5 - Critical  
    </dl>

    The default setting is 2. Setting this property is optional for the app.

In each of the example code snippets following, the calling application can set or query the property.



<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<tbody>
<tr class="odd">

<td>Android</td>

</tr>
<tr class="even">
<td>Enable automatic logging<br/></td>
<td><span data-codelanguage=""></span>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><pre><code>SharedPreferences preferences = PreferenceManager.getDefaultSharedPreferences(context);
SharedPreferences.Editor editor = preferences.edit();
editor.putBoolean(&quot;IpcCustomerExperienceDataCollectionEnabled&quot;, true); 
editor.commit();</code></pre></td>
</tr>
</tbody>
</table>
</td>

</tr>
<tr class="odd">
<td><p>Get current logging control flag setting</p></td>
<td><div class="code">
<span data-codelanguage=""></span>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><pre><code>SharedPreferences preferences = PreferenceManager.getDefaultSharedPreferences(context);
Boolean isLogUploadEnabled = preferences.getBoolean(&quot;IpcCustomerExperienceDataCollectionEnabled&quot;, false);</code></pre></td>
</tr>
</tbody>
</table>

</div></td>

</tr>
</tbody>
</table>



 



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">

<td>iOS</td>
</tr>
<tr class="even">
<td>Enable automatic logging<br/></td>
<td><span data-codelanguage=""></span>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><pre><code>NSUserDefaults *prefs = [NSUserDefaults standardUserDefaults];
        [prefs setBool:FALSE forKey:@&quot;IpcCustomerExperienceDataCollectionEnabled”];
        [[NSUserDefaults standardUserDefaults] synchronize];</code></pre></td>
</tr>
</tbody>
</table>
</td>
</tr>
<tr class="odd">
<td><p>Get current logging control flag setting</p></td>
<td><div class="code">
<span data-codelanguage=""></span>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><pre><code>[[NSUserDefaults standardUserDefaults] boolForKey:@&quot;IpcCustomerExperienceDataCollectionEnabled&quot;];</code></pre></td>
</tr>
</tbody>
</table>

</div></td>
</tr>
<tr class="even">
<td><p>Set log level control</p></td>
<td><div class="code">
<span data-codelanguage=""></span>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><pre><code>NSUserDefaults *prefs = [NSUserDefaults standardUserDefaults];
[prefs setInteger:1 forKey:@&quot;IpcLogLevel”];
[[NSUserDefaults standardUserDefaults] synchronize];</code></pre></td>
</tr>
</tbody>
</table>

</div></td>
</tr>
<tr class="odd">
<td><p>Get log level control setting</p></td>
<td><div class="code">
<span data-codelanguage=""></span>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><pre><code>[[NSUserDefaults standardUserDefaults] boolForKey:@&quot;IpcLogLevel&quot;];</code></pre></td>
</tr>
</tbody>
</table>

</div></td>
</tr>
</tbody>
</table>



 



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">

<td>Windows</td>
</tr>
<tr class="even">
<td>Enable automatic logging<br/></td>
<td><span data-codelanguage=""></span>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><pre><code>CustomerExperienceConfiguration::Option = CustomerExperienceOptions::LoggingEnabledNow;</code></pre></td>
</tr>
</tbody>
</table>

<p>For more information on optional settings, see [<strong>CustomerExperienceOptions</strong>](customerexperienceoptions.md).</p></td>
</tr>
<tr class="odd">
<td><p>Get current logging control flag setting</p></td>
<td><div class="code">
<span data-codelanguage=""></span>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><pre><code>CustomerExperienceOptions loggingOption = CustomerExperienceConfiguration::Option;</code></pre></td>
</tr>
</tbody>
</table>

</div></td>
</tr>
</tbody>
</table>



 

> [!Note]  
> The Windows code snips above are in C++. For C#, update the syntax with ‘.’ in place of ‘::’.

 

**Linux / C++** - This SDK has some basic logging that is not as extensive as that of the other platforms. For more information see the **Troubleshooting** section of the "README.md" at [RMS SDK for portable C++](https://github.com/AzureAD/rms-sdk-for-cpp#troubleshooting).

 

 





