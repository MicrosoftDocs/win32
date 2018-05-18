---
title: Enumerating Sinks
description: Enumerating Sinks
ms.assetid: '1b635cd8-6bdd-4592-bfb5-bcdcf7818e18'
keywords: ["Advanced Systems Format (ASF),enumerating sinks", "ASF (Advanced Systems Format),enumerating sinks", "Advanced Systems Format (ASF),sinks", "ASF (Advanced Systems Format),sinks", "sinks,enumerating"]
---

# Enumerating Sinks

The writer can have many sinks associated with it. You can enumerate the sinks that have been added to the writer by using [**IWMWriterAdvanced::GetSinkCount**](iwmwriteradvanced-getsinkcount.md) and [**IWMWriterAdvanced::GetSink**](iwmwriteradvanced-getsink.md).

The example code in the [Getting Error Messages from a Sink](getting-error-messages-from-a-sink.md) demonstrates sink enumeration.

> [!Note]  
> When enumerating sinks, the default file sink created in response to a call to [**IWMWriter::SetOutputFilename**](iwmwriter-setoutputfilename.md) will be enumerated along with any other sinks you have added. If you are using only the default file sink, you can access it by calling **GetSink** for sink index 0.

 

## Related topics

<dl> <dt>

[**IWMWriterAdvanced Interface**](iwmwriteradvanced.md)
</dt> <dt>

[**Working with Writer Sinks**](working-with-writer-sinks.md)
</dt> </dl>

 

 




