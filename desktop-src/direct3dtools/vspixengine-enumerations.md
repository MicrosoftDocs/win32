---
Description: The following enumerations are declared in vspixengine.h.
MS-HAID: vspixengine.vspixengine\_enumerations
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: Direct3D Diagnostics Capture Interface Enumerations
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# <span id="vspixengine.vspixengine_enumerations"></span>Direct3D Diagnostics Capture Interface Enumerations

The following enumerations are declared in vspixengine.h.

## <span id="in_this_section"></span>In this section

<table><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><thead><tr class="header"><th>Topic</th><th>Description</th></tr></thead><tbody><tr class="odd"><td><p>[<strong>Xml_Resource_Ids</strong>](https://msdn.microsoft.com/library/windows/desktop/mt432866)</p></td><td><p>Resource string ids set by caller to be returned in xml data for visualizing objects</p></td></tr><tr class="even"><td><p>[<strong>Resource_Id</strong>](https://msdn.microsoft.com/library/windows/desktop/mt432856)</p></td><td><p>Defines resource IDs for shared string resources. These are passed to the capture engine from the host. They are used to display strings to the HUD overlay of the app being captured or to pass registry values from Visual Studio options to the capture engi</p></td></tr><tr class="odd"><td><p>[<strong>Hresult</strong>](https://msdn.microsoft.com/library/windows/desktop/mt422645)</p></td><td><p>Custom HRESULT values for the graphics diagnostics capture interface.</p></td></tr><tr class="even"><td><p>[<strong>RemoteCommandType</strong>](https://msdn.microsoft.com/library/windows/desktop/mt432853)</p></td><td><p>An enum used to communicate between the capture engine and a host (such as Visual Studio Graphics Diagnostics).</p></td></tr><tr class="odd"><td><p>[<strong>CallbackCommandType</strong>](https://msdn.microsoft.com/library/windows/desktop/mt422630)</p></td><td><p>An enum used to communicate between the capture engine and a host (such as Visual Studio Graphics Diagnostics).</p></td></tr><tr class="even"><td><p>[<strong>PixPipeResponse</strong>](https://msdn.microsoft.com/library/windows/desktop/mt432849)</p></td><td><p>An enum used to send responses from the capture engine to Graphics Diagnostics.</p></td></tr><tr class="odd"><td><p>[<strong>REMOTINGVERSION</strong>](https://msdn.microsoft.com/library/windows/desktop/mt432854)</p></td><td><p>An enum used to indicate which version of the remoting protocul is being used.</p></td></tr><tr class="even"><td><p>[<strong>PIXELKILLREASON</strong>](https://msdn.microsoft.com/library/windows/desktop/mt432840)</p></td><td><p>An enum used to indicate why a pixel was rejected.</p></td></tr><tr class="odd"><td><p>[<strong>PIXELHISTORYFLAGS</strong>](https://msdn.microsoft.com/library/windows/desktop/mt432837)</p></td><td><p>An enum containing flags used to describe a pixel history result. See PixelHistoryOperation.</p></td></tr><tr class="even"><td><p>[<strong>EVENTCOLUMNID</strong>](https://msdn.microsoft.com/library/windows/desktop/mt422639)</p></td><td><p>An enum used to indicate well-known column IDs; these are column IDs that all implementations should support.</p></td></tr><tr class="odd"><td><p>[<strong>OBJECTSTATETYPE</strong>](https://msdn.microsoft.com/library/windows/desktop/mt432829)</p></td><td><p>Internal</p></td></tr><tr class="even"><td><p>[<strong>OBJECTTABLECOLUMNID</strong>](https://msdn.microsoft.com/library/windows/desktop/mt432830)</p></td><td><p>An enum used to indicate properties of data returned from an object table request. For more information, see IObjectTableRequest.</p></td></tr><tr class="odd"><td><p>[<strong>PIPELINESTAGES</strong>](https://msdn.microsoft.com/library/windows/desktop/mt432836)</p></td><td><p>An enum used to indicate a stage of the graphics pipeline.</p></td></tr><tr class="even"><td><p>[<strong>CHECKSUMALGORITHM</strong>](https://msdn.microsoft.com/library/windows/desktop/mt422632)</p></td><td><p>An enum used to indicate the checksum algorithm to be used.</p></td></tr><tr class="odd"><td><p>[<strong>EVENTTYPE</strong>](https://msdn.microsoft.com/library/windows/desktop/mt422640)</p></td><td><p>An enum used to indicate the type of an event.</p></td></tr><tr class="even"><td><p>[<strong>DESCRIPTOR_HEAP_HEADER_COLUMNS</strong>](https://msdn.microsoft.com/library/windows/desktop/mt422637)</p></td><td><p>An enum used to indicate a coumn header in the Descriptor heap viewer</p></td></tr><tr class="odd"><td><p>[<strong>DESCRIPTOR_HEAP_COLUMNS</strong>](https://msdn.microsoft.com/library/windows/desktop/mt422636)</p></td><td><p>An enum used to indicate a column in the Descriptor heap viewer.</p></td></tr><tr class="even"><td><p>[<strong>EXPERIMENTTYPE</strong>](https://msdn.microsoft.com/library/windows/desktop/mt422644)</p></td></tr><tr class="odd"><td><p>[<strong>DUMPERTYPE</strong>](https://msdn.microsoft.com/library/windows/desktop/mt422638)</p></td><td><p>An enum used to indicate what type of buffer IGenericBufferDataRequest returns.</p></td></tr><tr class="even"><td><p>[<strong>EXPERIMENTTRIGGERTYPE</strong>](https://msdn.microsoft.com/library/windows/desktop/mt422643)</p></td></tr><tr class="odd"><td><p>[<strong>REGISTER_FORMAT</strong>](https://msdn.microsoft.com/library/windows/desktop/mt432852)</p></td><td><p>Internal</p></td></tr><tr class="even"><td><p>[<strong>PRIMITIVE_TOPOLOGY</strong>](https://msdn.microsoft.com/library/windows/desktop/mt432851)</p></td><td><p>An enum used to indicate the topology of a mesh. See MeshDataVertCallback.</p></td></tr><tr class="odd"><td><p>[<strong>OFFLINEANALYSISSTAGE</strong>](https://msdn.microsoft.com/library/windows/desktop/mt432832)</p></td><td><p>An enum used to indicate stages of progress in frame analysis.</p></td></tr><tr class="even"><td><p>[<strong>OFFLINEANALYSISSOURCE</strong>](https://msdn.microsoft.com/library/windows/desktop/mt432831)</p></td><td><p>An enum used to indicate the source of graphics information for frame analysis.</p></td></tr></tbody></table>

 

## <span id="related_topics"></span>Related topics

[Direct3D Diagnostics Capture Interface Reference](vspixengine-reference.md)

 

 



