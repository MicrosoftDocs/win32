---
title: ITsSbTarget TargetName property
description: Specifies or retrieves the name of the target.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'ba5c3158-b4bc-457f-94ea-adb2e0852129'
ms.prod: 'windows-server-dev'
ms.technology: 'remote-desktop-services'
ms.tgt_platform: multiple
keywords: ["TargetName property Remote Desktop Services", "TargetName property Remote Desktop Services , ITsSbTarget interface", "ITsSbTarget interface Remote Desktop Services , TargetName property", "TargetName property Remote Desktop Services , ITsSbTargetEx interface", "ITsSbTargetEx interface Remote Desktop Services , TargetName property"]
topic_type:
- apiref
api_name:
- ITsSbTarget.TargetName
- ITsSbTarget.get_TargetName
- ITsSbTarget.put_TargetName
- ITsSbTargetEx.TargetName
- ITsSbTargetEx.get_TargetName
- ITsSbTargetEx.put_TargetName
api_location:
- Sbtsv.idl
api_type:
- COM
---

# ITsSbTarget::TargetName property

Specifies or retrieves the name of the target.

This property is read/write.

## Syntax


```C++
HRESULT put_TargetName(
  [in]          BSTR Val
);

HRESULT get_TargetName(
  [out, retval] BSTR *pVal
);
```



## Property value

A **BSTR** variable that specifies the target name.

## Remarks

This property was read-only prior to Windows Server 2012.

## Requirements



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Minimum supported client<br/></td>
<td>None supported<br/></td>
</tr>
<tr class="even">
<td>Minimum supported server<br/></td>
<td>Windows Server 2012<br/></td>
</tr>
<tr class="odd">
<td>IDL<br/></td>
<td><dl> <dt>Sbtsv.idl</dt> </dl></td>
</tr>
<tr class="even">
<td>IID<br/></td>
<td>IID_ITsSbTarget is defined as:
<ul>
<li>16616ECC-272D-411D-B324-126893033856</li>
<li>e85e10ea-db0b-4752-b456-5fd5840901c0 on Windows Server 2008 R2</li>
</ul></td>
</tr>
</tbody>
</table>



## See also

<dl> <dt>

[**ITsSbTargetEx**](itssbtargetex.md)
</dt> <dt>

[**ITsSbTarget**](itssbtarget.md)
</dt> </dl>

 

 





