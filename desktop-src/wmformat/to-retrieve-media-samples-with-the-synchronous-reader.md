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
ms.date: 05/31/2018
---

# To Retrieve Media Samples with the Synchronous Reader

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

 

 




