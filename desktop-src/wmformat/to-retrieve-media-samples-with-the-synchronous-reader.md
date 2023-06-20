---
title: To Retrieve Media Samples with the Synchronous Reader
description: To Retrieve Media Samples with the Synchronous Reader
ms.assetid: 7e228a0b-e29d-485e-b2ef-81c0311ca828
keywords:
- Advanced Systems Format (ASF),retrieving media samples
- ASF (Advanced Systems Format),retrieving media samples
- Advanced Systems Format (ASF),synchronous readers
- ASF (Advanced Systems Format),synchronous readers
- synchronous readers,retrieving media samples
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# To Retrieve Media Samples with the Synchronous Reader

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

You must request each sample one at a time from the synchronous reader. This gives you more control over the samples you receive and when you receive them.

Use the [**IWMSyncReader::GetNextSample**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmsyncreader-getnextsample) method to retrieve a sample. You need to pass mostly pointers to variables that will be filled with information about the sample retrieved as parameters. The only input parameter is *wStreamNum*. If you pass a stream number, **GetNextSample** will retrieve the next sample with the specified stream number. If you pass zero for *wStreamNum*, the next sample that occurs chronologically in the file is retrieved.

By default, the synchronous reader retrieves all of the samples from the outputs in a file in chronological order. If you call **GetNextSample** and there are no more samples to get, it will return NS\_E\_NO\_MORE\_SAMPLES, which is a failed error code. When coding therefore, you can simply loop through samples until the method fails.

> [!Note]  
> To ensure that the synchronous reader delivers correct sample durations for video streams, you must first configure the stream output. Call the [**IWMSyncReader::SetOutputSetting**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmsyncreader-setoutputsetting) method to set the g\_wszVideoSampleDurations setting to **TRUE**.

 

Example Code

The following example code shows how to use **GetNextSample** to retrieve all samples in a file.


```C++
// Loop through all the samples in the file.
do
{
   // Get the next sample.
   hr = pSyncReader->GetNextSample(0,
                                   &pMyBuffer,
                                   &cnsSampleTime,
                                   &cnsSampleDuration,
                                   &dwFlags,
                                   &dwOutputNumber,
                                   NULL);

   if(SUCCEEDED(hr))
   {
      // TODO: Process the sample in whatever way is appropriate 
      // to your application. When finished, clean up.
      pMyBuffer->Release();
      pMyBuffer = NULL;
      cnsSampleTime     = 0;
      cnsSampleDuration = 0;
      dwFlags           = 0;
      dwOutputNumber    = 0;
   }
} 
while (SUCCEEDED(hr));

```



## Related topics

<dl> <dt>

[**IWMSyncReader Interface**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmsyncreader)
</dt> <dt>

[**Reading Files with the Synchronous Reader**](reading-files-with-the-synchronous-reader.md)
</dt> </dl>

 

 




