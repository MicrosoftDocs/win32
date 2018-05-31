---
title: IVMKeyboard HasExclusiveAccess property
description: The HasExclusiveAccess property contains whether this IVMKeyboard object has exclusive control over the virtual machine's keyboard device.
ms.assetid: 94523158-1731-4f15-98d6-a3baf113d608
keywords:
- HasExclusiveAccess property Virtual Server
- HasExclusiveAccess property Virtual Server , IVMKeyboard interface
- IVMKeyboard interface Virtual Server , HasExclusiveAccess property
- HasExclusiveAccess property Virtual Server , VMKeyboard interface
- VMKeyboard interface Virtual Server , HasExclusiveAccess property
topic_type:
- apiref
api_name:
- IVMKeyboard.HasExclusiveAccess
- IVMKeyboard.get_HasExclusiveAccess
- IVMKeyboard.put_HasExclusiveAccess
- VMKeyboard.HasExclusiveAccess
api_location:
- VsComInterfaces.h
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IVMKeyboard::HasExclusiveAccess property

The **HasExclusiveAccess** property contains whether this [**IVMKeyboard**](ivmkeyboard.md) object has exclusive control over the virtual machine's keyboard device.

This property is read/write.

## Syntax


```C++
HRESULT put_HasExclusiveAccess(
  [in]  VARIANT_BOOL makeExclusive
);

HRESULT get_HasExclusiveAccess(
  [out] VARIANT_BOOL *isExclusive
);
```

<span codelanguage="VisualBasic"></span>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>VB</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><pre><code>VMKeyboard.HasExclusiveAccess( _
  ByRef isExclusive, _
  ByVal makeExclusive _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

Contains **vbTrue** if exclusive access to the virtual machine's keyboard device has been acquired, **vbFalse** otherwise.

This property value is read/write.

## Error codes



| Name                                                                                                               | Meaning                                                                                                                                                                                                                                           |
|--------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>                                   | The operation was successful.<br/>                                                                                                                                                                                                          |
| <dl> <dt>E\_POINTER</dt> </dl>                              | The *isExclusive* parameter is **NULL**.<br/>                                                                                                                                                                                               |
| <dl> <dt>S\_FALSE</dt> </dl>                                | The requested exclusive mode is already set for this device. This could happen when trying to set exclusive mode when it has already been acquired, or when trying to release exclusive mode when it had not been previously acquired.<br/> |
| <dl> <dt>VM\_E\_UNABLE\_TO\_SET\_EXCLUSIVE\_MODE</dt> </dl> | Failed to set or release exclusive mode as requested. This could be because the virtual machine is no longer running, or because another process has already acquired exclusive mode on the virtual machine's keyboard device.<br/>         |
| <dl> <dt> DISP\_E\_EXCEPTION</dt> </dl>                     | An unexpected error occurred.<br/>                                                                                                                                                                                                          |



## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMKeyboard**](ivmkeyboard.md)
</dt> </dl>

 

 





