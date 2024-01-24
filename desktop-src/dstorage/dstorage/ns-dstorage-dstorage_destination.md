---
UID: NS:dstorage.DSTORAGE_DESTINATION
ms.topic: reference
tech.root: dstorage
title: DSTORAGE_DESTINATION
ms.date: 08/25/2022
targetos: Windows
description: Describes the destination for a DirectStorage request.
prerelease: false
req.construct-type: structure
req.ddi-compliance: 
req.dll: 
req.header: dstorage.h
req.include-header: 
req.kmdf-ver: 
req.lib: 
req.max-support: 
req.redist: 
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.target-type: 
req.typenames: 
req.umdf-ver: 
req.unicode-ansi: 
topic_type:
 - apiref
api_type:
 - HeaderDef
api_location:
 - dstorage.h
api_name:
 - DSTORAGE_DESTINATION
f1_keywords:
 - DSTORAGE_DESTINATION
 - dstorage/DSTORAGE_DESTINATION
dev_langs:
 - c++
helpviewer_keywords:
 - DSTORAGE_DESTINATION
---

# DSTORAGE_DESTINATION union (dstorage.h)

Describes the destination for a DirectStorage request. For a request, the value of `request.Options.DestinationType` determines which of these union fields is active. See [IDStorageQueue::EnqueueRequest](nf-dstorage-idstoragequeue-enqueuerequest.md). 

## Syntax

```cpp
union DSTORAGE_DESTINATION {
  DSTORAGE_DESTINATION_MEMORY                Memory;
  DSTORAGE_DESTINATION_BUFFER                Buffer;
  DSTORAGE_DESTINATION_TEXTURE_REGION        Texture;
  DSTORAGE_DESTINATION_MULTIPLE_SUBRESOURCES MultipleSubresources;
  DSTORAGE_DESTINATION_TILES                 Tiles;
};
```

## Members

`Memory`

See [DSTORAGE_DESTINATION_MEMORY](ns-dstorage-dstorage_destination_memory.md).

`Buffer`

See [DSTORAGE_DESTINATION_BUFFER](ns-dstorage-dstorage_destination_buffer.md).

`Texture`

See [DSTORAGE_DESTINATION_TEXTURE_REGION](ns-dstorage-dstorage_destination_texture_region.md).

`MultipleSubresources`

See [DSTORAGE_DESTINATION_MULTIPLE_SUBRESOURCES](ns-dstorage-dstorage_destination_multiple_subresources.md).

`Tiles`

See [DSTORAGE_DESTINATION_TILES](ns-dstorage-dstorage_destination_tiles.md).

## Requirements

| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | dstorage.h |
