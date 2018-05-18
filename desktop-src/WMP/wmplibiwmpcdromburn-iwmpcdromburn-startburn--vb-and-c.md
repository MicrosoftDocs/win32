---
title: IWMPCdromBurn startBurn method
description: The startBurn method burns the CD.
ms.assetid: 'e852c011-5f54-469f-aead-37fa711ef876'
keywords: ["startBurn method Windows Media Player", "startBurn method Windows Media Player , IWMPCdromBurn interface", "IWMPCdromBurn interface Windows Media Player , startBurn method"]
topic_type:
- apiref
api_name:
- IWMPCdromBurn.startBurn
api_location:
- Interop.WMPLib.dll
api_type:
- COM
---

# IWMPCdromBurn::startBurn method

The **startBurn** method burns the CD.

## Syntax


```CSharp
public void startBurn();
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
<td><pre><code>Public Sub startBurn()
Implements IWMPCdromBurn.startBurn</code></pre></td>
</tr>
</tbody>
</table>



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Remarks

The value of **burnstate** should be wmpbsReady or wmpbsStopped before calling this method.

This method will not work if the CD drive is not a burner, or if the disc in the drive is not writable. Use **isAvailable** to determine whether a CD can be burned.

## Requirements



|                      |                                                                                                                        |
|----------------------|------------------------------------------------------------------------------------------------------------------------|
| Version<br/>   | Windows Media Player 11.<br/>                                                                                    |
| Namespace<br/> | **WMPLib**<br/>                                                                                                  |
| Assembly<br/>  | <dl> <dt>Interop.WMPLib.dll (Interop.WMPLib.dll.dll)</dt> </dl> |



## See also

<dl> <dt>

[**IWMPCdromBurn Interface (VB and C#)**](iwmpcdromburn--vb-and-c.md)
</dt> <dt>

[**IWMPCdromBurn.burnState (VB and C#)**](wmplibiwmpcdromburn-iwmpcdromburn-burnstate--vb-and-c.md)
</dt> <dt>

[**IWMPCdromBurn.isAvailable (VB and C#)**](wmplibiwmpcdromburn-iwmpcdromburn-isavailable--vb-and-c.md)
</dt> <dt>

[**IWMPCdromBurn.stopBurn (VB and C#)**](wmplibiwmpcdromburn-iwmpcdromburn-stopburn-iwmpcdromburn.md)
</dt> </dl>

 

 





