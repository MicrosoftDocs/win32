---
title: SetVarConversionLocaleSetting function
description: Sets National Language Support (NLS) flags to a specific locale for use when converting the date and time for the current user and computer.
ms.assetid: '2c238d3b-b607-4663-bd2f-2a200dcde253'
keywords: ["SetVarConversionLocaleSetting function Automation"]
topic_type:
- apiref
api_name:
- SetVarConversionLocaleSetting
api_location:
- OleAut32.dll
api_type:
- DllExport
---

# SetVarConversionLocaleSetting function

Sets National Language Support (NLS) flags to a specific locale for use when converting the date and time for the current user and computer.

## Syntax


```C++
HRESULT SetVarConversionLocaleSetting(
  _In_ ULONG dwFlags
);
```



## Parameters

<dl> <dt>

*dwFlags* \[in\]
</dt> <dd>

Determines the locale to use for date and time conversion. The values in the following table are used for this flag.



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
<td>Format is based on the current identity of the thread requesting these values. The current identity is based on the identity of the thread that makes the call to OleAut32.dll. <br/></td>
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

[**GetVarConversionLocaleSetting**](getvarconversionlocalesetting.md)
</dt> </dl>

 

 





