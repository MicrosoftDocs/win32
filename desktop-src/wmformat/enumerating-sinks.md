---
title: Enumerating Sinks
description: Enumerating Sinks
ms.assetid: 1b635cd8-6bdd-4592-bfb5-bcdcf7818e18
keywords:
- Advanced Systems Format (ASF),enumerating sinks
- ASF (Advanced Systems Format),enumerating sinks
- Advanced Systems Format (ASF),sinks
- ASF (Advanced Systems Format),sinks
- sinks,enumerating
ms.topic: article
ms.date: 05/31/2018
---

# Enumerating Sinks

The writer can have many sinks associated with it. You can enumerate the sinks that have been added to the writer by using [**IWMWriterAdvanced::GetSinkCount**](/previous-versions/windows/desktop/api/wmsdkidl/nf-wmsdkidl-iwmwriteradvanced-getsinkcount) and [**IWMWriterAdvanced::GetSink**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmwriteradvanced-getsink).

The example code in the [Getting Error Messages from a Sink](getting-error-messages-from-a-sink.md) demonstrates sink enumeration.

> [!Note]  
> When enumerating sinks, the default file sink created in response to a call to [**IWMWriter::SetOutputFilename**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmwriter-setoutputfilename) will be enumerated along with any other sinks you have added. If you are using only the default file sink, you can access it by calling **GetSink** for sink index 0.

 

## Related topics

<dl> <dt>

[**IWMWriterAdvanced Interface**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmwriteradvanced)
</dt> <dt>

[**Working with Writer Sinks**](working-with-writer-sinks.md)
</dt> </dl>

 

 




