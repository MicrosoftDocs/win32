---
title: About the dvr-ms File Format
description: About the dvr-ms File Format
ms.assetid: '10477644-2462-4264-b0c7-a22eaf754ace'
---

# About the dvr-ms File Format

Files created by the Stream Buffer Engine (SBE) are stored with the \*.dvr-ms file extension. When the SBE is being controlled from the Video Control, the audio and video elementary streams are examined for copy protection/control information. If this information does not specify that the content should be encrypted, then an unencrypted file will be created that can later be accessed by any DirectShow-based application that uses the SBE. If the information specifies that the content should be encrypted, then the resulting file will not be accessible, except for playback only on the same machine that was used to make the recording. DirectShow applications that are not based on the Video Control can use the SBE directly to create and play back unencrypted dvr-ms files.

This section contains the following topics:

-   [Playing \*.dvr-ms Files](playing---dvr-ms-files.md)
-   [Editing and Authoring dvr-ms Files](editing-and-authoring-dvr-ms-files.md)

## Related topics

<dl> <dt>

[Using the Stream Buffer Engine](using-the-stream-buffer-engine.md)
</dt> </dl>

 

 




