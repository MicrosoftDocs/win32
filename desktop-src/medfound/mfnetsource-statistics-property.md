---
description: Contains network statistics for the network source.
ms.assetid: 1948481b-febd-434b-a5dc-faef592ea0ed
title: MFNETSOURCE_STATISTICS Property (Mfidl.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MFNETSOURCE\_STATISTICS Property

Contains network statistics for the network source.

## Data Type

Varies; see Remarks.

## Remarks

The constant MFNETSOURCE\_STATISTICS defines a GUID that is used in conjunction with the [**MFNETSOURCE\_STATISTICS\_IDS**](/windows/desktop/api/mfidl/ne-mfidl-mfnetsource_statistics_ids) enumeration to define a set of property keys. Each property key in the set has **fmtid** equal to MFNETSOURCE\_STATISTICS and **pid** equal to one member of the enumeration. For more information, see [**MFNETSOURCE\_STATISTICS\_IDS**](/windows/desktop/api/mfidl/ne-mfidl-mfnetsource_statistics_ids).

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                     |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Mfidl.h</dt> </dl> |



## See also

<dl> <dt>

[Client Logging](client-logging.md)
</dt> <dt>

[Media Foundation Properties](media-foundation-properties.md)
</dt> <dt>

[Networking in Media Foundation](networking-in-media-foundation.md)
</dt> </dl>

 

 




