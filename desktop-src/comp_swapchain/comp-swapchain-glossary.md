---
title: Composition swapchain glossary
description: A glossary of composition swapchain terms. 
ms.topic: article
ms.date: 09/10/2021
---

# Composition swapchain glossary

|Term|Meaning|
|-|-|
|**Available (presentation buffer)**|A buffer that's safe for your application to render to without corrupting any previous presents. To be available, a buffer must have no previous presents that reference it that haven't entered into the retiring or retired state. A present may implicitly reference a buffer from a previous present if your application didn't update a surface, as is shown in the example in [Diagram of buffers, surfaces, and presents](comp-swapchain.md#diagram-of-buffers-surfaces-and-presents).|
|**Composition (presentation mode)**|A form of presentation in which the buffer presented by your application is copied into the backbuffer that DWM renders and sends to display hardware. This form of presentation has lower system requirements than direct scanout or iflip, but it's also less efficient.|
|**Composition Surface Handle**|A **HANDLE** that can bind a visual tree visual with a given swapchain, or presentation surface.|
|**Direct flip**|A form of presentation in which the buffer presentation by your application is sent directly to display hardware on systems that don't support multiplane overlay.|
|**Direct scanout**|A form of presentation in which the buffer presented by your application is not re-rendered into the buffer DWM sends to screen, but instead sent directly to the GPU scanout hardware. This might involve DWM assigning the buffer to a multiplane overlay plane, or it might be a mode in which the buffer is sent to the scanout hardware directly via *direct flip*. In a direct scanout presentation mode, DWM might be involved in programming the hardware to display the present, or it might be bypassed entirely when the system is in *iflip* mode.|
|**Front buffer rendering**|Drawing work issued for a buffer that is currently being displayed by the system. Depending on how the buffer is being displayed, this can result in corruption or an application hang, since Direct3D protects against issuing rendering work to buffers being displayed by scanout hardware.|
|**Hardware flip queue**|An operating system (OS) feature supported by some GPU hardware that allows GPUs to display presents independently, without CPU involvement, resulting in reduced power consumption, but potentially delaying CPU state updates such as buffer available events, present retiring fence, and present statistics.|
|**Independent flip (iflip)**|A more efficient method of direct scanout presentation in which the presents are sent directly to the GPU scanout hardware, completely bypassing the DWM. This form of presentation has higher system requirements, but allows for lower latencies, and system power savings.|
|**Multiplane overlay (MPO)**|A type of display hardware that is able to show multiple planes shown over top of one another. Presents from the presentation manager can be displayed as part of a plane in an MPO configuration to avoid needing to copy the presentation buffer into the backbuffer that DWM sends to the display hardware.|
|**Present**|A single instance of presentation. A present that is intended to show the results of a drawing operation to a single buffer to the screen.|
|**Present identifier (ID)**|An incrementing identifier, unique within a given presentation manager, associated with each present to allow it to be referred to by things such as  presentation statistics and present fences.|
|**Present queue**|A queue of presents that a presentation manager has issued but have yet to be processed by the system. All presents issued are processed in queue order, even if their target times are not increasing. That is to say, before present *n* can be process, present *n-1* must also be processed; so if subsequent presents have an earlier target time than a particular present, then they'll immediately override that particular present.|
|**(Present) target time**|The time at which a particular present should be shown on screen. The system will attempt to show the present as close to this time as it can.|
|**Presentation statistics**|information returned to your application that describe how a particular present was processed. Statistics are queued in the presentation manager to be read back by your application.|
|**Presentation surface**|a content placeholder that can be bound to a visual in a visual tree. A presentation surface can have a single displayed buffer at a time. Presentation manager presents will update the buffers for one or more presentation surfaces.|
|**Presentation**|The concept of showing the results of drawing operations on screen.|
|**Presentation buffer**|A Direct3D texture that has been associated with a presentation manager, and can therefore be presented by that presentation manager to screen.|
|**Visual tree**|A tree of visuals that describes an application's layout. The composition swapchain API issues presents to one or more visuals in a visual tree. For more information, see [**Windows.UI.Composition**](/uwp/api/windows.ui.composition) and [**DirectComposition**](/windows/win32/directcomp/directcomposition-portal) API documentation.|
|**VSync interrupt**|when a GPU displays a present, it issues a VSync interrupt to awaken the CPU to notify it that that present took place. This allows the CPU to update state such as the buffer available events, the present retiring fence, and present statistics. If the GPU supports hardware flip queue, your application can explicitly control which presents should force a VSync interrupt and immediately update state, and which presents should not, allowing for improved power efficiency at the expense of delayed feedback.|

## Related topics

* [Composition swapchain](comp-swapchain-portal.md)
