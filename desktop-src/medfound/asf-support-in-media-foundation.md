---
description: ASF Support in Media Foundation
ms.assetid: 4b0c4a83-623a-4378-9436-35ed120316af
title: ASF Support in Media Foundation
ms.topic: article
ms.date: 05/31/2018
---

# ASF Support in Media Foundation

Media Foundation supports media files in the Advanced Systems Format (ASF):

-   Windows Media Video (WMV files)
-   Windows Media Audio (WMA files)

Media Foundation provides several objects for reading and writing ASF files. These objects are provided in two different architectural layers.

First, the *pipeline* layer contains objects that work inside the [Media Foundation pipeline](media-foundation-pipeline.md) and conform to the APIs defined by the pipeline. The ASF pipeline layer contains:

-   [ASF Media Source](asf-media-source.md): Parses ASF files and delivers the audio/video data packets.
-   [Windows Media Codecs](windows-media-codecs.md): Decode or encode Windows Media audio or video streams.
-   [ASF Media Sink](asf-media-sinks.md): Receives data packets and writes an ASF file.

Second, the WM Container layer provides low-level control over parsing and writing an ASF file. The pipeline layer uses WMContainer internally. Applications can also use WMContainer for low-level ASF parsing and writing.

![diagram showing elements of the pipeline layer and the wm container](images/asf-components.png)

## In this section



| Topic                                                                         | Description                                                                                                        |
|-------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|
| [ASF File Structure](asf-file-structure.md)<br/>                       | Overview of the ASF file structure and the objects provided by Media Foundation to work with ASF files.<br/> |
| [Pipeline Layer ASF Components](pipeline-layer-asf-components.md)<br/> | Describes how to parse and author ASF files using the pipeline layer.<br/>                                   |
| [WMContainer ASF Components](wmcontainer-asf-components.md)<br/>       | Describes how to parse and author ASF files using the WMContainer layer.<br/>                                |



 

For detailed information about the structure of an ASF file, see the ASF specification, which can be downloaded from this [Microsoft website](https://www.microsoft.com/downloads/details.aspx?displaylang=en&FamilyID=56de5ee4-51ca-46c6-903b-97390ad14fea).

## Related topics

<dl> <dt>

[Media Foundation Programming Guide](media-foundation-programming-guide.md)
</dt> </dl>

 

 




