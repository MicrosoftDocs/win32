---
title: Configuration Common to All Streams
description: Configuration Common to All Streams
ms.assetid: 63e655b7-a4ef-4580-a0f3-03cedd2cbf9a
keywords:
- profiles,configurations common to all streams
- streams,common configurations
- streams,names
- streams,connection names
- streams,numbers
ms.topic: article
ms.date: 05/31/2018
---

# Configuration Common to All Streams

All streams, regardless of type, should be assigned a stream name, a connection name, and a stream number.

The stream name is simply a descriptive name you assign to the stream. A stream does not need to have a stream name, but it helps you to identify the stream when editing the profile at a later time. You can set a name for the stream by calling [**IWMStreamConfig::SetStreamName**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmstreamconfig-setstreamname).

Every stream should have a connection name, also called an input name. When you set the profile in the writer object to write a file, the writer will associate each connection name with an input. To identify the inputs, you must call [**IWMInputMediaProps::GetConnectionName**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwminputmediaprops-getconnectionname) to retrieve the connection name. Typical connection names are simple descriptions of the content, such as "audio". If your profile contains streams that are mutually exclusive by bit rate, each of the mutually exclusive streams must have the same connection name. If they do not, the profile is invalid and will be rejected by the writer. You can set a connection name by calling [**IWMStreamConfig::SetConnectionName**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmstreamconfig-setconnectionname).

The stream number identifies the stream within the file. Unlike input numbers and output numbers, stream numbers start at 1, not 0. A stream number is different than a stream index, which you use when getting streams in a profile by using [**IWMProfile::GetStream**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmprofile-getstream). The stream index is a number assigned to the stream by the profile object. Stream indexes range between 0 and one less than the number of streams retrieved by [**IWMProfile::GetStreamCount**](/previous-versions/windows/desktop/api/wmsdkidl/nf-wmsdkidl-iwmprofile-getstreamcount). Stream numbers need not be sequential, though they usually are, and can range from 1 to 63. You can set a stream number by calling [**IWMStreamConfig::SetStreamNumber**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmstreamconfig-setstreamnumber).

## Related topics

<dl> <dt>

[**Configuring Streams**](configuring-streams.md)
</dt> <dt>

[**Inputs, Streams and Outputs**](inputs-streams-and-outputs.md)
</dt> </dl>

 

 




