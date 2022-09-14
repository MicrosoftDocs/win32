---
description: Reliability and Security
ms.assetid: 1cbfabce-3d56-4e23-b9a7-02369c67e392
title: Reliability and Security
ms.topic: article
ms.date: 05/31/2018
---

# Reliability and Security

Because Windows Imaging Component (WIC) codecs will be invoked from within the Windows shell and Photo Gallery, codec authors should make every effort to ensure a high level of reliability and security in their WIC codecs.

Writing reliable code largely depends on good coding practices, effective code reviews, and thorough unit testing and scenario testing. In addition, the following guidelines will help ensure that the codec complies with Windows Vista policies regarding reliability.

-   Enable I/O cancellation.

    Codec authors should provide a way for the end user to cancel any long-running operation. WIC codecs support this by implementing IWICBitmapProgressNotification. This allows a calling application to specify a callback function for the codec to call at specified intervals to notify the caller of the progress of the current operation. When an application returns ERROR\_CANCELLED from the callback function, the codec must cancel whatever operation is in progress and propagate the HRESULT back to the caller. This is especially important for RAW codecs, because it might take several seconds to decode a full-size RAW image and applications need a way to abort this processing.

-   Make sure that code runs in the smallest scope that is required to perform its function.

    Codec authors must ensure that the codec does not consume more resources than necessary or have a greater scope than is required. The scope of a codec in WIC is a single image file; the codec is created when an image file is loaded, and the codec is released when the image is closed. Because WIC is an extensible component-based platform, WIC codecs will have overlapping loads and unloads, and starts and stops, all within the same process. If the underlying infrastructure of a codec requires start and stop operations at a scope larger than a single image, reliability will be impacted. WIC-enabled codecs will be used by the Windows Explorer, as well as other applications. Therefore, if a codec remains loaded for the lifetime of the process, memory will not be released efficiently and a failure of the codec could hang Windows Explorer and potentially require the machine to be rebooted. (Consider that the codec will be invoked every time an image is thumbnailed for the first time in Windows Explorer: it is essential that this be a lightweight operation.)

-   Use static and dynamic code analysis tools.

    -   Static analysis tools:

        PREfix - for detecting errors at compile time.

        PREfast - for analyzing code for bugs.

    -   Dynamic analysis tools:

        AppVerifier - which helps make applications more resilient by simulating common real-world software issues.

-   Verify all inputs in code reviews.

    All parameters for exported methods and all file data must be carefully verified for validity and robustly rejected if faulty, in order to protect against buffer overruns and underruns, arithmetic overflows and underflows, and unexpected types.

-   Use file fuzzing techniques to discover potential crashes and hangs.

    File fuzzing is the process of testing the codec with randomly permuted inputs.

    There are two forms of file fuzzing: undirected (random) fuzzing and directed fuzzing. Undirected fuzzing does some random bit flipping to see if random input can crash the codec. Directed fuzzing permutes the input based on some knowledge of the file format. For example, if there is a cycle redundancy check (CRC) at byte offset 32, then changing any bytes without updating the CRC will likely not exercise most of the codepaths. In this example, a directed fuzzer should fix the CRC when any bytes are modified.

    The input set of images for file fuzzing should be created so that each parameter combination that the decoder supports is tested. For example, if the decoder supports little- and big-endian files and three compression settings, then the input set of image should consist of little-endian files of each compression setting and big-endian files for each compression setting. This approach will yield a large, but very robust set of input images to be tested. Even if no camera produces each of the combinations but the decoder supports these theoretical combinations, codec authors should fuzz these inputs.

    Security can be greatly enhanced by regularly performing fuzz testing of image files during codec development. Codecs should always be able to detect image file corruption and fail gracefully in the case of a malformed request or of malformed data.

-   Stress the code.

    Stress-test the codec by running it continually in multiple simultaneous processes, performing all supported operations in all possible sequences, on images of varying sizes (including very large images) from every supported camera.

-   Thread safety.

    As of Windows 7, WIC requires that RAW CODECs be of COM apartment type "Both". This means that you must do the appropriate locking to handle cross-apartment callers and callers in multi-threaded scenarios. Objects within an Multi Threaded Apartment (MTA) may be called concurrently by any number of threads within the MTA, allowing for better performance on multi-core systems and certain server scenarios. In addition, WIC CODECs that live within an MTA can call other objects that live within the MTA without the marshalling cost associated of calling between threads that live in different STA apartments. In Windows 7, all in-box WIC CODECs have been updated to support MTAs, including JPEG, TIFF, PNG, GIF, ICO, and BMP. 3rd-party CODECs that do not to support MTAs will cause significant performance costs in multithreaded applications due to marshaling. Enabling MTA support requires proper synchronization to be implemented in the 3rd-party CODEC. Exact implementation of these synchronization techniques is beyond the scope of this paper. A general reference for synchronizing COM objects is provided below.

    https://msdn.microsoft.com/library/ms809971.aspx

## Related topics

<dl> <dt>

**Conceptual**
</dt> <dt>

[Windows Imaging Component Overview](-wic-about-windows-imaging-codec.md)
</dt> <dt>

[WIC Guidelines for Camera RAW Image Formats](-wic-rawguidelines.md)
</dt> <dt>

[How to Write a WIC-Enabled CODEC](-wic-howtowriteacodec.md)
</dt> </dl>

 

 



