---
title: To Seek to Markers
description: To Seek to Markers
ms.assetid: '2d5efebf-dcbd-4fb8-933e-cc6d3a99adf8'
keywords: ["Advanced Systems Format (ASF),seeking to markers", "ASF (Advanced Systems Format),seeking to markers", "Advanced Systems Format (ASF),asynchronous readers", "ASF (Advanced Systems Format),asynchronous readers", "Advanced Systems Format (ASF),markers", "ASF (Advanced Systems Format),markers", "asynchronous readers,seeking to markers", "asynchronous readers,markers", "markers,seeking", "markers,asynchronous readers"]
---

# To Seek to Markers

A marker is a named location in an ASF file. You can only start playback from the location of a marker by using the asynchronous reader. You can begin playback at a marker by following these steps.

1.  Call **IWMReader::QueryInterface** to obtain a pointer to the [**IWMHeaderInfo**](iwmheaderinfo.md) interface.
2.  Retrieve the total number of markers in the file by calling [**IWMHeaderInfo::GetMarkerCount**](iwmheaderinfo-getmarkercount.md).
3.  Loop through the markers, using the marker count retrieved in step 2. Retrieve the name and time of each marker by calling [**IWMHeaderInfo::GetMarker**](iwmheaderinfo-getmarker.md) for each. Save the index of the desired marker.
4.  Call **IWMReader::QueryInterface** to obtain a pointer to the [**IWMReaderAdvanced2**](iwmreaderadvanced2.md) interface.
5.  Specify the marker at which to start playback by calling [**IWMReaderAdvanced2::StartAtMarker**](iwmreaderadvanced2-startatmarker.md). You must pass the index of the desired marker, which you saved in step 3.
6.  Handle the samples as you normally would in your implementation of the [**IWMReaderCallback::OnSample**](iwmreadercallback-onsample.md) method.

## Related topics

<dl> <dt>

[**Markers**](markers.md)
</dt> <dt>

[**Reading Files with the Asynchronous Reader**](reading-files-with-the-asynchronous-reader.md)
</dt> <dt>

[**Working with Indexes**](working-with-indexes.md)
</dt> </dl>

 

 




