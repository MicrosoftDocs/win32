---
title: IVMMouse UsingAbsoluteCoordinates property
description: The UsingAbsoluteCoordinates property contains TRUE if the mouse device is set to use absolute coordinates, FALSE if set to use delta coordinates.
ms.assetid: '15707ad2-e450-4cb4-b396-6b74e7992848'
keywords: ["UsingAbsoluteCoordinates property Virtual Server", "UsingAbsoluteCoordinates property Virtual Server , IVMMouse interface", "IVMMouse interface Virtual Server , UsingAbsoluteCoordinates property", "UsingAbsoluteCoordinates property Virtual Server , VMMouse interface", "VMMouse interface Virtual Server , UsingAbsoluteCoordinates property"]
topic_type:
- apiref
api_name:
- IVMMouse.UsingAbsoluteCoordinates
- IVMMouse.get_UsingAbsoluteCoordinates
- IVMMouse.put_UsingAbsoluteCoordinates
- VMMouse.UsingAbsoluteCoordinates
api_location:
- VsComInterfaces.h
api_type:
- COM
---

# IVMMouse::UsingAbsoluteCoordinates property

The **UsingAbsoluteCoordinates** property contains **TRUE** if the mouse device is set to use absolute coordinates, **FALSE** if set to use delta coordinates. This property is local only to this object and will default to **FALSE** for a new [**IVMMouse**](ivmmouse.md) object. Note that Additions must be installed in order to use absolute coordinates.

This property is read/write.

## Syntax


```C++
HRESULT put_UsingAbsoluteCoordinates(
  [in]  VARIANT_BOOL usingAbsoluteCoordinates
);

HRESULT get_UsingAbsoluteCoordinates(
  [out] VARIANT_BOOL *usingAbsoluteCoordinates
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
<td><pre><code>VMMouse.UsingAbsoluteCoordinates( _
  ByRef usingAbsoluteCoordinates, _
  ByVal usingAbsoluteCoordinates _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

Contains **vbTrue** if the device is set to use absolute coordinates, **vbFalse** if it is set to use delta coordinates.

This property value is read/write.

## Error codes



| Name                                                                                                                 | Meaning                                                                                     |
|----------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>                                     | The operation was successful.<br/>                                                    |
| <dl> <dt> E\_POINTER</dt> </dl>                               | The parameter is **NULL**.<br/>                                                       |
| <dl> <dt>VM\_E\_ADDITIONS\_FEATURE\_NOT\_AVAILABLE</dt> </dl> | Additions are not installed. Additions are required to use absolute coordinates.<br/> |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl>                        | An unexpected error occurred.<br/>                                                    |



## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMMouse**](ivmmouse.md)
</dt> </dl>

 

 





