---
description: Specifies whether the topology loader enumerates the media types provided by the media source.
ms.assetid: 2675ef16-2018-47e8-bb22-2fc0d62e6681
title: MF_TOPOLOGY_ENUMERATE_SOURCE_TYPES attribute (Mfidl.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MF\_TOPOLOGY\_ENUMERATE\_SOURCE\_TYPES attribute

Specifies whether the topology loader enumerates the media types provided by the media source.

## Data type

**UINT32**

Use one of the following values.



| Value                                                                                                                                    | Meaning                                             |
|------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------|
| <span id="FALSE"></span><span id="false"></span><dl> <dt>****FALSE****</dt> </dl> | Do not enumerate the source media types.<br/> |
| <span id="TRUE"></span><span id="true"></span><dl> <dt>****TRUE****</dt> </dl>    | Enumerate the source media types.<br/>        |



 

## Get/set

To get this attribute, call [**IMFAttributes::GetUINT32**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-getuint32).

To set this attribute, call [**IMFAttributes::SetUINT32**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-setuint32).

## Applies to

[**IMFTopology**](/windows/desktop/api/mfidl/nn-mfidl-imftopology)

## Remarks

Each stream on a media source can offer more than one media type. The list of types is enumerated through the [**IMFMediaTypeHandler**](/windows/desktop/api/mfidl/nn-mfidl-imfmediatypehandler) interface on the stream descriptor.

The order in which the topology loader tries a media source's media types is controlled by two attributes:

-   The MF\_TOPOLOGY\_ENUMERATE\_SOURCE\_TYPES attribute on the topology.
-   The [**MF\_TOPONODE\_CONNECT\_METHOD**](mf-toponode-connect-method-attribute.md) attribute on the source node.

If the MF\_TOPOLOGY\_ENUMERATE\_SOURCE\_TYPES attribute is **FALSE** or not set, the topology loader uses the stream's current media type. It does not enumerate the list of possible types. If the current media type is incompatible with the downstream topology node, and no combination of decoders/converters can be found, topology resolution fails.

If the MF\_TOPOLOGY\_ENUMERATE\_SOURCE\_TYPES attribute is **TRUE**, the topology loader enumerates the source's media types until it finds a compatible type. In that case, the exact order of operations depends on the whether the [**MF\_TOPONODE\_CONNECT\_METHOD**](mf-toponode-connect-method-attribute.md) attribute on the source node includes the **MF\_CONNECT\_RESOLVE\_INDEPENDENT\_OUTPUTTYPES** flag.

If MF\_TOPOLOGY\_ENUMERATE\_SOURCE\_TYPES is **TRUE** and the **MF\_CONNECT\_RESOLVE\_INDEPENDENT\_OUTPUTTYPES** flag is set, the topology loader exhausts each media type before moving to the next, as follows:

``` syntax
foreach media type T
    connect directly using T
    if failed, connect with converters using T
    if failed, connect with decoders using T
```

If MF\_TOPOLOGY\_ENUMERATE\_SOURCE\_TYPES is **TRUE** but **MF\_CONNECT\_RESOLVE\_INDEPENDENT\_OUTPUTTYPES** is not set, the topology loader tries a direct connection with each media type, then tries each media type with converters, and finally tries each media type with decoders:

``` syntax
foreach media type T
    connect directly using T
if failed,
    foreach media type T
        connect with converters using T
if failed
    foreach media type T
        connect with decoders using T
```

If MF\_TOPOLOGY\_ENUMERATE\_SOURCE\_TYPES is **FALSE**, the **MF\_CONNECT\_RESOLVE\_INDEPENDENT\_OUTPUTTYPES** flag is ignored.

The default value of MF\_TOPOLOGY\_ENUMERATE\_SOURCE\_TYPES is **FALSE**, for compatibility with existing applications.

The GUID constant for this attribute is exported from mfuuid.lib.

### Example

Here is an example that illustrates the **MF\_CONNECT\_RESOLVE\_INDEPENDENT\_OUTPUTTYPES** flag. Assume the topology has the MF\_TOPOLOGY\_ENUMERATE\_SOURCE\_TYPES attribute set to **TRUE**.

The media source offers the following types:

-   T1, T2, T3

The media sink accepts the following types:

-   T3, T4

Case 1: The **MF\_CONNECT\_RESOLVE\_INDEPENDENT\_OUTPUTTYPES** flag is set.

1.  The topology loader tries a direct connection with T1. The sink rejects T1.
2.  The topology loader inserts a decoder that accepts T1 and outputs T4. The sink accepts T4.
3.  The final topology contains: media source → decoder → media sink.

Case 2: The flag is not set.

1.  The topology loader tries a direct connection with T1. The sink rejects T1.
2.  The topology loader tries a direct connection with T2. The sink rejects T2.
3.  The topology loader tries a direct connection with T3. The sink accepts T3.
4.  The final topology contains: media source → media sink.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                            |
| Header<br/>                   | <dl> <dt>Mfidl.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[Topology Attributes](topology-attributes.md)
</dt> </dl>

 

 




