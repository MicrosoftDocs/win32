---
Description: 'Note  This interface has been deprecated.'
ms.assetid: '64ee80cd-9f63-4f38-853a-1ecfc03e6076'
title: ICaptureGraphBuilder interface
---

# ICaptureGraphBuilder interface

> [!Note]  
> This interface has been deprecated. It will continue to be supported for backward compatibility with existing applications, but new applications should use the [**ICaptureGraphBuilder2**](icapturegraphbuilder2.md) interface.

 

The `ICaptureGraphBuilder` interface enables you to build capture graphs, preview graphs, file recompression graphs, or other custom graphs.

## Members

The **ICaptureGraphBuilder** interface inherits from the [**IUnknown**](com.iunknown) interface. **ICaptureGraphBuilder** also has these types of members:

-   [Methods](#methods)

### Methods

The **ICaptureGraphBuilder** interface has these methods.



| Method                                                              | Description                                                                                                                                                         |
|:--------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AllocCapFile**](icapturegraphbuilder-alloccapfile.md)           | Preallocates a capture file to a specified size.<br/>                                                                                                         |
| [**ControlStream**](icapturegraphbuilder-controlstream.md)         | Sends stream control messages to the pin of the specified category on one or more capture filters in a graph.<br/>                                            |
| [**CopyCaptureFile**](icapturegraphbuilder-copycapturefile.md)     | Copies the valid media data from the preallocated capture file.<br/>                                                                                          |
| [**FindInterface**](icapturegraphbuilder-findinterface.md)         | Looks for the specified interface on the filter, upstream and downstream from the filter, and, optionally, only on the output pin of the given category.<br/> |
| [**GetFiltergraph**](icapturegraphbuilder-getfiltergraph.md)       | Retrieves the filter graph that the builder is using.<br/>                                                                                                    |
| [**RenderStream**](icapturegraphbuilder-renderstream.md)           | Connects a source filter's pin, of an optionally specified category, to the rendering filter, and optionally through another filter.<br/>                     |
| [**SetFiltergraph**](icapturegraphbuilder-setfiltergraph.md)       | Tells the graph builder object which filter graph to use.<br/>                                                                                                |
| [**SetOutputFileName**](icapturegraphbuilder-setoutputfilename.md) | Creates the rendering section of the filter graph, which will save bits to disk with the specified file name.<br/>                                            |



 

## See also

<dl> <dt>

[Deprecated Interfaces](deprecated-interfaces.md)
</dt> </dl>

 

 




