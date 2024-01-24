---
description: This overview describes the Resource Interchange File Format (RIFF), which is used in .wav files. RIFF is the typical format from which audio data for XAudio2 will be loaded.
ms.assetid: b543e949-223c-ddd3-7527-a41f3709a0c1
title: Resource Interchange File Format (RIFF)
ms.topic: article
ms.date: 05/31/2018
---

# Resource Interchange File Format (RIFF)

This overview describes the Resource Interchange File Format (RIFF), which is used in .wav files. RIFF is the typical format from which audio data for XAudio2 will be loaded.

## RIFF

A RIFF file is composed of multiple discrete sections of data called *chunks*.

## FOURCC Identifiers

The type of data in a chunk is indicated by a four-character code (FOURCC) identifier. A FOURCC is a 32-bit unsigned integer created by concatenating four ASCII characters used to identify chunk types in a RIFF file. For example, the FOURCC "abcd" is represented on a little-endian system as 0x64636261. FOURCCs can contain space characters, so " abc" is a valid FOURCC. Audio files use FOURCC codes to identify audio format chunks, audio data chunks, and any other chunks specific to the audio format.

The following table shows the FOURCC identifiers that can be expected in the audio formats supported by XAudio2. 

| Format | FOURCC identifiers                     | Additional information                                                                               |
|--------|----------------------------------------|------------------------------------------------------------------------------------------------------|
| PCM    | "RIFF", "fmt" , "data"                 |                                                                                                      |
| ADPCM  | "RIFF", "fmt", "data", "smpl", "wsmpl" | See [ADPCM Overview](adpcm-overview.md) for a description of the ADPCM-specific FOURCC identifiers. |



 

The FOURCC identifiers "RIFF", "fmt", and "data" are common to all of the supported formats. The following table describes the FOURCC identifiers that are found in all of the supported formats. 

| FOURCC identifier | Description                                                                                                                                                                                                                        |
|-------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| "RIFF"            | Standard RIFF chunk containing a file type with the value of "WAVE" or "XWMA" in the first four bytes of its data section and the other chunks in the file in the remainder of its data section.                                   |
| "fmt"             | Contains the format header for the audio file. The data in this chunk corresponds to one of the following structures: **WAVEFORMATEX**, **WAVEFORMATEXTENSIBLE ADPCMWAVEFORMAT**.                                                  |
| "data"            | Contains audio data for the audio file. In XAudio2, the contents of the data chunk will be read into a buffer and passed to a source voice as the **pAudioData** member of an [**XAUDIO2\_BUFFER**](/windows/desktop/api/xaudio2/ns-xaudio2-xaudio2_buffer) structure. |



 

## Chunks

A RIFF file consists of a RIFF chunk containing zero or more other chunks.

-   The RIFF chunk has the following form:

    "RIFF", fileSize, fileType, data

    Where "RIFF" is the literal FOURCC code "RIFF", *fileSize* is a 4-byte value giving the size of the data in the file, and *fileType* is a FOURCC that identifies the specific file type. The value of *fileSize* includes the size of *fileType* FOURCC plus the size of the data that follows, but does not include the size of the "RIFF" FOURCC or the size of *fileSize*. The data consists of chunks in any order.

-   Other chunks have the following form:

    ```
    chunkID, chunkSize, data
    ```

    

    Where *chunkID* is a FOURCC that identifies the data contained in the chunk, *chunkSize* is a 4-byte value giving the size of the data section of the chunk, and data is zero or more bytes of data. The data is always padded to the nearest WORD boundary. *chunkSize* gives the size of the valid data in the chunk. It does not include the padding, the size of *chunkID*, or the size of *chunkSize*.

## Related topics

<dl> <dt>

[Getting Started](getting-started.md)
</dt> <dt>

[How to: Play a Sound with XAudio2](how-to--play-a-sound-with-xaudio2.md)
</dt> <dt>

[XAudio2 Programming Reference](programming-reference.md)
</dt> </dl>

 

 



