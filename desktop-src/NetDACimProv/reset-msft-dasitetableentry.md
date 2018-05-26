---
Description: Resets the configuration of the entry in the Direct Access site table.
ms.assetid: 12caa0cd-9cd6-4933-b6c4-330858f9c3e8
title: Reset method of the MSFT\_DASiteTableEntry class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Reset method of the MSFT\_DASiteTableEntry class

Resets the configuration of the entry in the Direct Access site table.

## Syntax


```mof
uint32 Reset(
  [in]  boolean               TeredoServerIP,
  [in]  boolean               IPHttpsProfile,
  [in]  boolean               GslbIP,
  [in]  boolean               PassThru,
  [out] MSFT_DASiteTableEntry OutputObject
);
```



## Parameters

<dl> <dt>

*TeredoServerIP* \[in\]
</dt> <dd>

Specifies whether to reset the **TeledoServerIP** property of the [**MSFT\_DASiteTableEntry**](msft-dasitetableentry.md) object.

</dd> <dt>

*IPHttpsProfile* \[in\]
</dt> <dd>

Specifies whether to reset the **IPHttpsProfile** property of the [**MSFT\_DASiteTableEntry**](msft-dasitetableentry.md) object.

</dd> <dt>

*GslbIP* \[in\]
</dt> <dd>

Specifies whether to reset the **GslbIP** property of the [**MSFT\_DASiteTableEntry**](msft-dasitetableentry.md) object.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

Specifies whether the method should output an object that represents the reset entry in the *OutputObject* parameter.

</dd> <dt>

*OutputObject* \[out\]
</dt> <dd>

Receives a [**MSFT\_DASiteTableEntry**](msft-dasitetableentry.md) object for the reset entry.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                          |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                          |
| MOF<br/>                      | <dl> <dt>NetDACim.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>NetDACim.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_DASiteTableEntry**](msft-dasitetableentry.md)
</dt> </dl>

 

 




