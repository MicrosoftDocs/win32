---
description: Topology Node Attributes
ms.assetid: 584c0670-9051-4d03-9635-c8fadc8798c3
title: Topology Node Attributes
ms.topic: article
ms.date: 05/31/2018
---

# Topology Node Attributes

The following attributes apply to topology nodes.

## General Topology Node Attributes



| Attribute                                                                       | Description                                                                                                                                              |
|---------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**MF\_TOPONODE\_CONNECT\_METHOD**](mf-toponode-connect-method-attribute.md)   | Specifies how the topology loader connects this topology node, and whether this node is optional.                                                        |
| [**MF\_TOPONODE\_DECODER**](mf-toponode-decoder-attribute.md)                  | Specifies whether a toplogy node's object is a decoder.                                                                                                  |
| [**MF\_TOPONODE\_DECRYPTOR**](mf-toponode-decryptor-attribute.md)              | Specifies whether a toplogy node's underlying object is a decryptor.                                                                                     |
| [**MF\_TOPONODE\_DISCARDABLE**](mf-toponode-discardable-attribute.md)          | Specifies whether the pipeline can drop samples from a topology node.                                                                                    |
| [**MF\_TOPONODE\_ERROR\_MAJORTYPE**](mf-toponode-error-majortype-attribute.md) | Contains the major media type for a topology node. This attribute is set when the topology fails to load because the correct decoder could not be found. |
| [**MF\_TOPONODE\_ERROR\_SUBTYPE**](mf-toponode-error-subtype-attribute.md)     | Contains the media subtype for a topology node. This attribute is set when the topology fails to load because the correct decoder could not be found.    |
| [**MF\_TOPONODE\_ERRORCODE**](mf-toponode-errorcode-attribute.md)              | Contains the error code from the most recent connection failure for this topology node.                                                                  |
| [**MF\_TOPONODE\_LOCKED**](mf-toponode-locked-attribute.md)                    | Specifies whether the media types can be changed on this topology node.                                                                                  |
| [**MF\_TOPONODE\_MARKIN\_HERE**](mf-toponode-markin-here-attribute.md)         | Specifies whether the pipeline applies mark-in at this node.                                                                                             |
| [**MF\_TOPONODE\_MARKOUT\_HERE**](mf-toponode-markout-here-attribute.md)       | Specifies whether the pipeline applies mark-out at this node.                                                                                            |



 

## Source Node Attributes



| Attribute                                                                                       | Description                                                                                                       |
|-------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| [**MF\_TOPONODE\_MEDIASTART**](mf-toponode-mediastart-attribute.md)                            | Specifies the start time of a presentation, relative to the start the media source file, in 100-nanosecond units. |
| [**MF\_TOPONODE\_MEDIASTOP**](mf-toponode-mediastop-attribute.md)                              | Specifies the stop time of a presentation, relative to the start the media source file, in 100-nanosecond units.  |
| [**MF\_TOPONODE\_PRESENTATION\_DESCRIPTOR**](mf-toponode-presentation-descriptor-attribute.md) | Contains a pointer to the presentation descriptor for the media source.                                           |
| [**MF\_TOPONODE\_SEQUENCE\_ELEMENTID**](mf-toponode-sequence-elementid-attribute.md)           | Specifies the element that contains a source node.                                                                |
| [**MF\_TOPONODE\_SOURCE**](mf-toponode-source-attribute.md)                                    | Contains a pointer to the media source associated with a topology node.                                           |
| [**MF\_TOPONODE\_STREAM\_DESCRIPTOR**](mf-toponode-stream-descriptor-attribute.md)             | Contains a pointer to the stream descriptor for the media source.                                                 |
| [**MF\_TOPONODE\_WORKQUEUE\_ID**](mf-toponode-workqueue-id-attribute.md)                       | Specifies a work queue for a topology node.                                                                       |
| [**MF\_TOPONODE\_WORKQUEUE\_MMCSS\_CLASS**](mf-toponode-workqueue-mmcss-class-attribute.md)    | Specifies a Multimedia Class Scheduler Service (MMCSS) task for a topology node.                                  |
| [**MF\_TOPONODE\_WORKQUEUE\_MMCSS\_TASKID**](mf-toponode-workqueue-mmcss-taskid-attribute.md)  | Specifies a MMCSS task identifier for a topology node.                                                            |



 

## Transform Node Attributes



| Attribute                                                                             | Description                                                                                                |
|---------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|
| [**MF\_TOPONODE\_D3DAWARE**](mf-toponode-d3daware-attribute.md)                      | Specifies whether the transform associated with a topology node supports DirectX Video Acceleration (DXVA) |
| [**MF\_TOPONODE\_DRAIN**](mf-toponode-drain-attribute.md)                            | Specifies when a transform is drained.                                                                     |
| [**MF\_TOPONODE\_FLUSH**](mf-toponode-flush-attribute.md)                            | Specifies when a transform is flushed.                                                                     |
| [**MF\_TOPONODE\_TRANSFORM\_OBJECTID**](mf-toponode-transform-objectid-attribute.md) | The class identifier (CLSID) of the transform associated with this topology node.                          |



 

## Output Node Attributes



| Attribute                                                                                  | Description                                                                                                      |
|--------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|
| [**MF\_TOPONODE\_DISABLE\_PREROLL**](mf-toponode-disable-preroll-attribute.md)            | Specifies whether the Media Session uses preroll on the media sink represented by this topology node.            |
| [**MF\_TOPONODE\_NOSHUTDOWN\_ON\_REMOVE**](mf-toponode-noshutdown-on-remove-attribute.md) | Specifies whether the Media Session shuts down the media sink when the output node is removed from the topology. |
| [**MF\_TOPONODE\_RATELESS**](mf-toponode-rateless-attribute.md)                           | Specifies whether the media sink associated with this topology node is rateless.                                 |
| [**MF\_TOPONODE\_STREAMID**](mf-toponode-streamid-attribute.md)                           | The stream identifier of the stream sink associated with this topology node.                                     |



 

## Tee Node Attributes



| Attribute                                                                  | Description                                                 |
|----------------------------------------------------------------------------|-------------------------------------------------------------|
| [**MF\_TOPONODE\_PRIMARYOUTPUT**](mf-toponode-primaryoutput-attribute.md) | Indicates which output is the primary output on a tee node. |



 

## Related topics

<dl> <dt>

[**IMFTopologyNode**](/windows/desktop/api/mfidl/nn-mfidl-imftopologynode)
</dt> <dt>

[Media Foundation Attributes](media-foundation-attributes.md)
</dt> <dt>

[Topology Attributes](topology-attributes.md)
</dt> </dl>

 

 



