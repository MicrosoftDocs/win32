---
title: GetVarConversionLocaleSetting function
description: Gets an Automation specific National Language Support (NLS) flag that defines the general behavior of Automation when formatting the date, time, numbers, currency for the current user and machine.
ms.assetid: 36f1857b-c56e-4ef5-a501-fcca386ace07
keywords:
- GetVarConversionLocaleSetting function Automation
topic_type:
- apiref
api_name:
- GetVarConversionLocaleSetting
api_location:
- OleAut32.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# GetVarConversionLocaleSetting function

Gets an Automation specific National Language Support (NLS) flag that defines the general behavior of Automation when formatting the date, time, numbers, currency for the current user and machine.

## Syntax


```C++
HRESULT GetVarConversionLocaleSetting(
  _Out_ ULONG *dwFlags
);
```



## Parameters

<dl> <dt>

*dwFlags* \[out\]
</dt> <dd>

Indicates the locale to use for date and time conversion. The values in the following table are used for this flag.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Value</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><dl> <dt>0</dt> </dl></td>
<td>The default value. It uses the locale set by the last user or process that set the cache.<br/></td>
</tr>
<tr class="even">
<td><dl> <dt>1</dt> </dl></td>
<td>Format is based on the current identity of the thread requesting these values. The current identity is based on the identity of the thread that makes the call to the OleAut32.dll. <br/></td>
</tr>
<tr class="odd">
<td><dl> <dt>2</dt> </dl></td>
<td>Format is forced to use the system default regional settings. The system default settings are set for a computer at reboot. In this case, the date format is not read from the registry but from the Locale.nls file for that locale.<br/>
<blockquote>
[!Note]<br />
Changing the default locale changes all regional settings (time, money, date formats, and so on). There is no way to modify a specific setting within the locale.
</blockquote>
<br/></td>
</tr>
</tbody>
</table>



 

</dd> </dl>

## Return value

If this function succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements



|                    |                                                                                         |
|--------------------|-----------------------------------------------------------------------------------------|
| Library<br/> | <dl> <dt>OleAut32.lib</dt> </dl> |
| DLL<br/>     | <dl> <dt>OleAut32.dll</dt> </dl> |



## See also

<dl> <dt>

[**SetVarConversionLocaleSetting**](setvarconversionlocalesetting.md)
</dt> </dl>

 

 





