---
description: AVI RIFF File Reference
ms.assetid: 2d8cf5be-1252-4b58-89b1-f5c53ea17d0e
title: AVI RIFF File Reference
ms.topic: article
ms.date: 05/31/2018
---

# AVI RIFF File Reference

The Microsoft AVI file format is a RIFF file specification used with applications that capture, edit, and play back audio-video sequences. In general, AVI files contain multiple streams of different types of data. Most AVI sequences use both audio and video streams. A simple variation for an AVI sequence uses video data and does not require an audio stream.

This section does not describe the OpenDML AVI file format extensions. For further information on these extensions, see *OpenDML AVI File Format Extensions*, published by the OpenDML AVI M-JPEG File Format Subcommittee.

## FOURCCs

A FOURCC (four-character code) is a 32-bit unsigned integer created by concatenating four ASCII characters. For example, the FOURCC 'abcd' is represented on a Little-Endian system as 0x64636261. FOURCCs can contain space characters, so ' abc' is a valid FOURCC. The AVI file format uses FOURCC codes to identify stream types, data chunks, index entries, and other information.

## RIFF File Format

The AVI file format is based on the RIFF (resource interchange file format) document format. A RIFF file consists of a RIFF header followed by zero or more *lists* and *chunks*.

-   The RIFF header has the following form:

    `'RIFF' fileSize fileType (data)`

    where 'RIFF' is the literal FOURCC code 'RIFF', `fileSize` is a 4-byte value giving the size of the data in the file, and `fileType` is a FOURCC that identifies the specific file type. The value of `fileSize` includes the size of the `fileType` FOURCC plus the size of the data that follows, but does not include the size of the 'RIFF' FOURCC or the size of `fileSize`. The file data consists of chunks and lists, in any order.

-   A chunk has the following form:

    `ckID ckSize ckData`

    where `ckID` is a FOURCC that identifies the data contained in the chunk, `ckSize` is a 4-byte value giving the size of the data in `ckData`, and `ckData` is zero or more bytes of data. The data is always padded to nearest **WORD** boundary. `ckSize` gives the size of the valid data in the chunk; it does not include the padding, the size of `ckID`, or the size of `ckSize`.

-   A list has the following form:

    `'LIST' listSize listType listData`

    where 'LIST' is the literal FOURCC code 'LIST', `listSize` is a 4-byte value giving the size of the list, `listType` is a FOURCC code, and `listData` consists of chunks or lists, in any order. The value of `listSize` includes the size of `listType` plus the size of `listData`; it does not include the 'LIST' FOURCC or the size of `listSize`.

The remainder of this section uses the following notation to describe RIFF chunks:

`ckID ( ckData )`

where the chunk size is implicit. Using this notation, a list can be represented as:

`'LIST' ( listType ( listData ) )`

Optional elements are placed in brackets: `[ optional element ]`

## AVI RIFF Form

AVI files are identified by the FOURCC 'AVI ' in the RIFF header. All AVI files include two mandatory LIST chunks, which define the format of the streams and the stream data, respectively. An AVI file might also include an index chunk, which gives the location of the data chunks within the file. An AVI file with these components has the following form:


```C++
RIFF ('AVI '
      LIST ('hdrl' ... )
      LIST ('movi' ... )
      ['idx1' (<AVI Index>) ]
     )
```



The 'hdrl' list defines the format of the data and is the first required LIST chunk. The 'movi' list contains the data for the AVI sequence and is the second required LIST chunk. The 'idx1' list contains the index. AVI files must keep these three components in the proper sequence.

> [!Note]  
> The OpenDML extensions define another type of index, identified by the FOURCC 'indx'.

 

The 'hdrl' and 'movi' lists use subchunks for their data. The following example shows the AVI RIFF form expanded with the chunks needed to complete these lists:


```C++
RIFF ('AVI '
      LIST ('hdrl'
            'avih'(<Main AVI Header>)
            LIST ('strl'
                  'strh'(<Stream header>)
                  'strf'(<Stream format>)
                  [ 'strd'(<Additional header data>) ]
                  [ 'strn'(<Stream name>) ]
                  ...
                 )
             ...
           )
      LIST ('movi'
            {SubChunk | LIST ('rec '
                              SubChunk1
                              SubChunk2
                              ...
                             )
               ...
            }
            ...
           )
      ['idx1' (<AVI Index>) ]
     )
```



## AVI Main Header

The 'hdrl' list begins with the main AVI header, which is contained in an 'avih' chunk. The main header contains global information for the entire AVI file, such as the number of streams within the file and the width and height of the AVI sequence. The main header chunk consists of an [**AVIMAINHEADER**](/previous-versions/windows/desktop/api/Aviriff/ns-aviriff-avimainheader) structure.

## AVI Stream Headers

One or more 'strl' lists follow the main header. A 'strl' list is required for each data stream. Each 'strl' list contains information about one stream in the file, and must contain a stream header chunk ('strh') and a stream format chunk ('strf'). In addition, a 'strl' list might contain a stream-header data chunk ('strd') and a stream name chunk ('strn').

The stream header chunk ('strh') consists of an [**AVISTREAMHEADER**](/previous-versions/windows/desktop/api/avifmt/ns-avifmt-avistreamheader) structure.

A stream format chunk ('strf') must follow the stream header chunk. The stream format chunk describes the format of the data in the stream. The data contained in this chunk depends on the stream type. For video streams, the information is a [**BITMAPINFO**](/windows/win32/api/wingdi/ns-wingdi-bitmapinfoheader) structure, including palette information if appropriate. For audio streams, the information is a [**WAVEFORMATEX**](/previous-versions/dd757713(v=vs.85)) structure.

If the stream-header data ('strd') chunk is present, it follows the stream format chunk. The format and content of this chunk are defined by the codec driver. Typically, drivers use this information for configuration. Applications that read and write AVI files do not need to interpret this information; they simple transfer it to and from the driver as a memory block.

The optional 'strn' chunk contains a null-terminated text string describing the stream.

The stream headers in the 'hdrl' list are associated with the stream data in the 'movi' list according to the order of the 'strl' chunks. The first 'strl' chunk applies to stream 0, the second applies to stream 1, and so forth.

## Stream Data ('movi' List)

Following the header information is a 'movi' list that contains the actual data in the streams—that is, the video frames and audio samples. The data chunks can reside directly in the 'movi' list, or they might be grouped within 'rec ' lists. The 'rec ' grouping implies that the grouped chunks should be read from disk all at once, and is intended for files that are interleaved to play from CD-ROM.

The FOURCC that identifies each data chunk consists of a two-digit stream number followed by a two-character code that defines the type of information in the chunk.



| Two-character code | Description              |
|--------------------|--------------------------|
| db                 | Uncompressed video frame |
| dc                 | Compressed video frame   |
| pc                 | Palette change           |
| wb                 | Audio data               |



 

For example, if stream 0 contains audio, the data chunks for that stream would have the FOURCC '00wb'. If stream 1 contains video, the data chunks for that stream would have the FOURCC '01db' or '01dc'. Video data chunks can also define new palette entries to update the palette during an AVI sequence. Each palette-change chunk ('xxpc') contains an [**AVIPALCHANGE**](/previous-versions/windows/desktop/api/avifmt/ns-avifmt-avipalchange) structure. If a stream contains palette changes, set the **AVISF\_VIDEO\_PALCHANGES** flag in the **dwFlags** member of the [**AVISTREAMHEADER**](/previous-versions/windows/desktop/api/avifmt/ns-avifmt-avistreamheader) structure for that stream.

Text streams can use arbitrary two-character codes.

## AVI Index Entries

<dl> <dt>

<span id="AVI_1.0_index"></span><span id="avi_1.0_index"></span><span id="AVI_1.0_INDEX"></span>AVI 1.0 index
</dt> <dd>

An optional index ('idx1') chunk can follow the 'movi' list. The index contains a list of the data chunks and their location in the file. It consists of an [**AVIOLDINDEX**](/previous-versions/windows/desktop/api/Aviriff/ns-aviriff-avioldindex) structure with entries for each data chunk, including 'rec ' chunks. If the file contains an index, set the **AVIF\_HASINDEX** flag in the **dwFlags** member of the [**AVIMAINHEADER**](/previous-versions/windows/desktop/api/Aviriff/ns-aviriff-avimainheader) structure.

</dd> <dt>

<span id="AVI_2.0_index"></span><span id="avi_2.0_index"></span><span id="AVI_2.0_INDEX"></span>AVI 2.0 index
</dt> <dd>

An AVI 2.0 index can appear as a single chunk. Alternatively, index segments can be interleaved within the 'movi' chunk. If the index segments are placed in the 'movi' chunk, a super index contains an index of the index segments. The [**AVIMETAINDEX**](/previous-versions/windows/desktop/api/aviriff/ns-aviriff-avimetaindex) structure is the base structure for both the index segments and the super index. For more information, see the *OpenDML AVI File Format Extensions*, published by the OpenDML AVI M-JPEG File Format Subcommittee. (This resource may not be available in some languages and countries.)

</dd> </dl>

## Other Data Chunks

Data can be aligned in an AVI file by inserting 'JUNK' chunks as needed. Applications should ignore the contents of a 'JUNK' chunk.

## Related topics

<dl> <dt>

[AVI File Format](avi-file-format.md)
</dt> </dl>

 

 
