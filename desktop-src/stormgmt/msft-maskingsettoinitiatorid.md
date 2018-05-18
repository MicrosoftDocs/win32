---
title: MSFT\_MaskingSetToInitiatorId class
description: Association between MaskingSet and InitiatorId.
ms.assetid: '8D2D62DE-D7DB-4E22-9704-017B586988BE'
keywords: ["MSFT_MaskingSetToInitiatorId class Windows Storage Management API", "MSFT_MaskingSetToInitiatorId class Windows Storage Management API , described"]
topic_type:
- apiref
api_name:
- MSFT_MaskingSetToInitiatorId
- MSFT_MaskingSetToInitiatorId.MaskingSet
- MSFT_MaskingSetToInitiatorId.InitiatorId
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
---

# MSFT\_MaskingSetToInitiatorId class

Association between [**MaskingSet**](msft-maskingset.md) and [**InitiatorId**](msft-initiatorid.md).

The following syntax is simplified from Managed Object Format (MOF) code.

## Syntax

``` syntax
[Association]
class MSFT_MaskingSetToInitiatorId
{
  MSFT_MaskingSet  REF MaskingSet;
  MSFT_InitiatorId REF InitiatorId;
};
```

## Members

The **MSFT\_MaskingSetToInitiatorId** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_MaskingSetToInitiatorId** class has these properties.

<dl> <dt>

**InitiatorId**
</dt> <dd> <dl> <dt>

Data type: **MSFT\_InitiatorId**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

</dd> <dt>

**MaskingSet**
</dt> <dd> <dl> <dt>

Data type: **MSFT\_MaskingSet**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>Storagewmi.mof</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_InitiatorId**](msft-initiatorid.md)
</dt> <dt>

[**MSFT\_MaskingSet**](msft-maskingset.md)
</dt> </dl>

 

 





