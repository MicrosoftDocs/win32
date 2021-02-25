---
description: The &\#0034;leaky bucket&\#0034; model is a way to model the buffering requirements for smooth playback.
ms.assetid: 2f7f80d6-3abb-462f-a571-b223a1d59da6
title: The Leaky Bucket Buffer Model (Microsoft Media Foundation)
ms.topic: article
ms.date: 05/31/2018
---

# The Leaky Bucket Buffer Model (Microsoft Media Foundation)

When you stream media over a network, the decoder receives encoded data at a theoretically constant rate (the transmission rate). The decoder consumes this data to produce decoded output. In the general case, however, the decoder consumes the data at a *variable* rate, because then encoder can use a variable encoding rate.

The "leaky bucket" model is a way to model the buffering requirements for smooth playback. In this model, the decoder maintains a buffer. Encoded data goes from the network into the buffer, and from the buffer into the decoder. If the buffer underflows, it means the decoder is removing data from the buffer faster than the network is delivering it. If the buffer overflows, it means the network is delivering data faster than the decoder consumes it.

This topic describes the "leaky bucket" model of buffers for encoding and decoding.

-   [The Leaky Bucket](#the-leaky-bucket)
-   [The Bucket in Use](#the-bucket-in-use)
-   [Setting Leaky Bucket Values for ASF Streams](#setting-leaky-bucket-values-for-asf-streams)
-   [Leaky Bucket Values in the ASF Multiplexer](#leaky-bucket-values-in-the-asf-multiplexer)
-   [Updating Leaky Bucket Values in the ASF Media Sink](#updating-leaky-bucket-values-in-the-asf-media-sink)
-   [Related topics](#related-topics)

## The Leaky Bucket

To understand the leaky bucket model, consider a bucket with a small hole at the bottom. Three parameters define the bucket:

-   The capacity (B)
-   The rate at which water flows out of the bucket (R)
-   The initial fullness of the bucket (F)

In this metaphor, the bucket is the buffer:

![illustration showing a buffer as a bucket, input rate as water entering the bucket, and output rate as water leaving through a hole in the bucket](images/asf-components03.png)

If water is poured into the bucket at exactly rate *R*, the bucket will remain at F, because the input rate equals the output rate. If the input rate increases while *R* remains constant, the bucket accumulates water. If the input rate is larger than *R* for a sustained period, eventually the bucket overflows. However, the input rate can vary around *R* without overflowing the bucket, as long as the average input rate does not exceed the capacity of the bucket. The larger the capacity, the more the input rate can vary within a given window of time.

In ASF, the leaky bucket is defined by three parameters:

-   The average bit rate, in bytes per second, which corresponds to the output rate (*R*)
-   The buffer window, measured in milliseconds, which corresponds to the bucket capacity (*B*).
-   The initial buffer fullness, which is generally set to zero.

The bit rate measures the average number of bits per second in the encoded stream. The buffer window measures the number of milliseconds of data at that bit rate that can fit in the buffer. The size of the buffer in bits is equal to R \* (B / 1000).

ASF payload data may enter the leaky bucket at irregular times and in irregular amounts, but must leave the bucket at a constant positive bit rate. Because of the buffer window, there is a possible delay between the time that payload enters the bucket and when it leaves. The maximum delay that can occur is *B*/*R*. The payload data that enters into the bucket is according to the presentation time and must never overflow the bucket. In addition to the presentation time, each payload also has a send time—the time at which the payload data leaves the bucket according to the bit rate. Send time must be earlier than the presentation time to ensure that, when the leaky bucket gets close to being full, every payload leaves the bucket before or at its presentation time. To accomplish this, the presentation times are shifted ahead by the *B*/*R* value (the *preroll*), and the send times get a head start starting at zero. The send time must be no later than the presentation time because that would indicate that the payload entered the bucket too late and cannot be included in the data object. The preroll value is included in the [ASF Header Object](asf-file-structure.md) .

For glitch-free streaming over the network, compressed streams within the media content must maintain a constant bit rate throughout the playback duration. The ASF leaky bucket model ensures that media data is sent across the network at a constant bit rate. The parameters of the leaky bucket are specified in the Extended Stream Properties Object of the [ASF Header Object](asf-file-structure.md). In Microsoft Media Foundation, they are set as attributes on the media type that represents the stream.

The leaky bucket values are defined both in the ASF file sink and the underlying ASF multiplexer object, and the Windows Media encoder. These values could be same or different. For example, consider a streaming scenario, which requires the audio samples to be delivered later than the video samples so that the file can be streamed without latency. To achieve this, the audio stream's leaky bucket in the media sink can be set to a value higher than the value set in the Windows Media audio encoder.

To set B/R values in the encoder, the application must set the [**MFPKEY\_RAVG**](mfpkey-ravgproperty.md), [**MFPKEY\_BAVG**](mfpkey-bavgproperty.md), [**MFPKEY\_RMAX**](mfpkey-rmaxproperty.md), and [**MFPKEY\_BMAX**](mfpkey-bmaxproperty.md) properties. For information about setting properties in the encoder, see [Encoding Properties](configuring-the-encoder.md).

## The Bucket in Use

The goal of an encoder is to ensure that the content never overflows the buffer. The encoder uses the bit rate and buffer window values as guides. The actual number of bits passed over any period of time equal to the buffer window can never be greater than twice the size of the buffer.

Consider the following example: You have a 3-gallon bucket with a hole in it through which 1 gallon can flow per minute. You put the bucket under a spigot and open the valve to let out water at a rate of 1 gallon per minute. The water flows out of the bucket as quickly as it enters, leaving no extra in the bucket. Then you increase the flow from the spigot to 2 gallons per minute. Each minute that the water flows at this rate, 2 gallons go into the bucket and 1 gallon leaks out, leaving 1 gallon in the bucket. At the end of 3 minutes, 6 gallons of water have gone into the bucket, 3 gallons have leaked out, and the bucket is full.

In practice, the theoretical maximum data rate over an interval equal to the buffer window is never achieved. The previous example assumed a constant data rate. Given the same 3-gallon bucket, you could increase the flow rate from the spigot to 6 gallons per minute for one minute and then turn the spigot off for two minutes. Even though the total amount of water put into the bucket is within the theoretical maximum for the buffer window, the concentration of that amount into one part of the window causes the bucket to overflow. At 6 gallons per minute, the 3-gallon bucket overflows shortly after 30 seconds pass. Therefore, the actual maximum amount of data that can be delivered to the buffer over the duration of any interval equal to the buffer window setting depends upon the size of individual samples and when they are delivered.

So far the examples have only discussed the buffer used by the decoder, but a leaky bucket buffer is also used by the encoder which creates the compressed content. The encoder makes whatever adjustments are necessary to the compression algorithms to keep the bit rate of the compressed samples within the boundaries described by the bit rate and buffer window, assuming that the samples will be delivered to the decoder at a constant rate. You can think of the encoder bucket as mirroring the decoder bucket. The encoder bucket is filled at a variable rate determined by the size of the individual samples and leaks at a constant rate equal to the average bit rate.

Consider the following example of an encoder and decoder connected together over a network. You encode a video file at 30 frames per second with a bit rate of 6,000 bits per second and a buffer window of 3 seconds (a total buffer size of 18,000 bits). The first sample is encoded as a key frame and takes up 7,000 bits. The encoder buffer now contains 7,000 bits. The next 29 frames are all delta frames that total 3,000 bits. So the first second of content (30 frames) would put the buffer fullness at 10,000 bits if nothing were leaking out. We know that the bit rate of the stream is 6,000 bits per second, so after the first second of encoded content is put in the encoder buffer, the fullness drops to 4,000 bits. In the decoding application, this stream is delivered to the decoder buffer at 6,000 bits per second. After one second, the buffer contains 6,000 bits. The first sample contains 7,000 bits, so the decoder buffer must be filled more before the decoder begins removing samples.

## Setting Leaky Bucket Values for ASF Streams

In a file-encoding scenario, an application can set the leaky bucket values while configuring the streams in the [ASF Profile](asf-profile.md).

After you have created the stream and have a reference to the stream's [**IMFASFStreamConfig**](/windows/desktop/api/wmcontainer/nn-wmcontainer-imfasfstreamconfig) interface, you can set the values by using the following attributes:

-   [**MF\_ASFSTREAMCONFIG\_LEAKYBUCKET1**](mf-asfstreamconfig-leakybucket1-attribute.md) (average leaky bucket values)
-   [**MF\_ASFSTREAMCONFIG\_LEAKYBUCKET2**](mf-asfstreamconfig-leakybucket2-attribute.md) (maximum leaky bucket values)

For information about adding streams and getting the **IMFASFStreamConfig** pointer, see [Adding Stream Information to the ASF File Sink](adding-stream-information-to-the-asf-file-sink.md).

These values contain the following set of information:

-   Average bit rate: Get the average bit rate from the output media type that is selected during media type negotiation. Use the [**MF\_MT\_AUDIO\_AVG\_BYTES\_PER\_SECOND**](mf-mt-audio-avg-bytes-per-second-attribute.md) attribute (for audio streams) or the [**MF\_MT\_AVG\_BITRATE**](mf-mt-avg-bitrate-attribute.md) attribute (for video streams).
-   Buffer window: If you have an instance of the encoder and have negotiated output media types, you can update this value later by querying the encoder for the [**IWMCodecLeakyBucket**](/windows/desktop/api/wmcodecdsp/nn-wmcodecdsp-iwmcodecleakybucket) interface and then calling [**IWMCodecLeakyBucket::GetBufferSizeBits**](../wmformat/iwmcodecleakybucket-getbuffersizebits.md) (wmcodecifaces.h, wmcodecdspuuid.lib). Otherwise, Use the default value of 3000 milliseconds.
-   Initial buffer size: Set to 0.

The values provided by the application depend on the type of encoding and the media type of the stream. For example, [Constant Bit Rate Encoding](constant-bit-rate-encoding.md) requires a predetermined fixed bit rate and a buffer window. The application can specify these leaky bucket values by setting the [**MFPKEY\_VIDEOWINDOW**](mfpkey-videowindowproperty.md) encoding property and the [**MF\_ASFSTREAMCONFIG\_LEAKYBUCKET1**](mf-asfstreamconfig-leakybucket1-attribute.md) attribute on the stream. The specified buffer window values are used to make sure that the encoded file has the correct send times marked on the data packets and the preroll value appears in the ASF Header Object. It is sufficient to set **MF\_ASFSTREAMCONFIG\_LEAKYBUCKET1** because these specified values are copied into the [**MF\_ASFSTREAMCONFIG\_LEAKYBUCKET2**](mf-asfstreamconfig-leakybucket2-attribute.md) attribute.

For 2-pass encoding modes you need to set both of these attributes to specify the average and maximum values.

For VBR encoding, the application can query for the leaky bucket values used by the encoder only after the encoding pass is complete. Therefore, while configuring the media sink, the application can choose not to set the attributes or properties related to leaky buckets. After encoding, the application must query the encoder for the [**MFPKEY\_RAVG**](mfpkey-ravgproperty.md), [**MFPKEY\_BAVG**](mfpkey-bavgproperty.md), [**MFPKEY\_RMAX**](mfpkey-rmaxproperty.md), and [**MFPKEY\_BMAX**](mfpkey-bmaxproperty.md) properties and set them in the media sink so that the accurate values are reflected in the Header Object. For code example about how to update the values for VBR encoding, see "Update Encoding Properties in the File Sink" in [Tutorial: 1-Pass Windows Media Encoding](tutorial--1-pass-windows-media-encoding.md).

If you are copying Windows Media content from source to media sink without encoding, the leaky bucket values must be set in the media sink.

## Leaky Bucket Values in the ASF Multiplexer

In Media Foundation, the leaky bucket values are used by the [ASF Multiplexer](asf-multiplexer.md) to set up the internal leaky bucket values that it uses to generate data packets. The payload is contained within a media sample and a series of media samples constitutes an ASF data packet. Based on the leaky bucket values and the presentation time, the multiplexer assigns a send time for each media sample so that the bit rates of the packets being sent across the network is at a constant bit rate (*R*).

An application cannot set leaky bucket values in the multiplexer directly. The values must be provided on the ASF media sink, which sets the appropriate values on the multiplexer. The values set in [**MF\_ASFSTREAMCONFIG\_LEAKYBUCKET1**](mf-asfstreamconfig-leakybucket1-attribute.md) and [**MF\_ASFSTREAMCONFIG\_LEAKYBUCKET2**](mf-asfstreamconfig-leakybucket2-attribute.md) are used by the multiplexer to validate the samples sent to the ASF media sink are generated by using the specified values.

## Updating Leaky Bucket Values in the ASF Media Sink

An application can overwrite the stream-level leaky bucket values (set in the ASF profile during stream creation) by setting the [**MFPKEY\_ASFSTREAMSINK\_CORRECTED\_LEAKYBUCKET**](mfpkey-asfstreamsink-corrected-leakybucket-property.md) property in the media sink's property store. To get a reference to the property store, use the ContentInfo object implemented by the media sink. For more information, see [Setting Properties in the File Sink](setting-properties-in-the-file-sink.md).

**Note**  This operation is only allowed for audio streams.

This property must be set after you have set the output type on the encoder. Based on the bit rate set in the media type, the encoder calculates the buffer size to ensure that the generated media samples never overflow the buffer. The encoder makes necessary adjustments during compression to keep the bit rate of the compressed samples within the boundaries described by the bit rate and buffer window.

Similar to the stream configuration attributes for leaky buckets, set the average bit rate and the buffer size, and the initial buffer fullness in an array of DWORDs. For more information, see "Setting Leaky Bucket Values for ASF Streams" section in this topic.

## Related topics

<dl> <dt>

[ASF Support in Media Foundation](asf-support-in-media-foundation.md)
</dt> <dt>

[Windows Media Codecs](windows-media-codecs.md)
</dt> </dl>

 

 
