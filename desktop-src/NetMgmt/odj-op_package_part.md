---
title: OP_PACKAGE_PART
description: OP_PACKAGE_PART IDL Definition
ms.assetid: 8f13aa71-a7b2-41ee-ad1e-4953f49a391a
ms.topic: reference
ms.date: 10/12/2020
ms.reviewer: jsimmons
---

# OP_PACKAGE_PART structure

Defines a structure that contains a data set identified by a GUID.

## Syntax

```C++
typedef struct _OP_PACKAGE_PART
{
    GUID    PartType;
    ULONG   ulFlags;
    OP_BLOB Part;
    OP_BLOB Extension;
} OP_PACKAGE_PART, *POP_PACKAGE_PART;
```

## Members

### PartType

Identifies the serialized structure contained in Part per the following table:

|PartType|Meaning|
| --- | --- |
|GUID_JOIN_PROVIDER {631c7621-5289-4321-bc9e-80f843f868c3}|Contains a serialized ODJ_WIN7_BLOB structure.|
|GUID_JOIN_PROVIDER2 {57BFC56B-52F9-480C-ADCB-91B3F8A82317}|Contains a serialized OP_JOIN_PROV2_PART structure.|
|GUID_JOIN_PROVIDER3 {FC0CCF25-7FFA-474A-8611-69FFE269645F}|Contains a serialized OP_JOIN_PROV3_PART structure.|
|GUID_JOIN_PROVIDER4 {4A08716A-6710-4647-8211-FDBB0B03F60B}|Contains a serialized OP_JOIN_PROV4_PART structure.|
|GUID_CERT_PROVIDER	{9c0971e9-832f-4873-8e87-ef1419d4781e}|Contains a serialized OP_CERT_PART structure.|
|GUID_POLICY_PROVIDER {68fb602a-0c09-48ce-b75f-07b7bd58f7ec}|Contains a serialized OP_POLICY_PART structure.|

### ulFlags

Must be set to zero or more of the following flags:

|Value|Meaning|
| --- | --- |
|OPSPI_PACKAGE_PART_ESSENTIAL (0x00000001)|This package part is considered essential. If the consumer does not recognize this package part or fails to successfully process it, the overall operation must fail.|

### Part

Contains a serialized structure in an OP_BLOB structure. The specific structure is determined by PartType.

### Extension

Reserved for future use and MUST be set to all zeros.

## See also

[**Offline Domain Join IDL Definitions**](odj-idl.md)

[**OP\_BLOB**](odj-op_blob.md)
