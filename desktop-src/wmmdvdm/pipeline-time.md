---
title: PIPELINE\_TIME
description: The PIPELINE\_TIME class describes either a frame presentation time or the duration of a transition or effect.
ms.assetid: '13b50545-b3d2-45aa-8f89-07699d7ec9ca'
keywords: ["PIPELINE_TIME Windows Movie Maker and DVD Maker"]
topic_type:
- apiref
api_name:
- PIPELINE_TIME
api_location:
- GPUPipelineTime.h
api_type:
- HeaderDef
---

# PIPELINE\_TIME

The **PIPELINE\_TIME** class describes either a frame presentation time or the duration of a transition or effect. You should not need to create the class or modify its values, but you should know how to read values from it. This section covers only the basic information you need to know to get data from a **PIPELINE\_TIME** object. If you need more details on the class, you can examine the class definition in PipelineTime.h.

**PIPELINE\_TIME** objects can store data in two formats: absolute time (fractions of a second), and frame rate (frames per second).

-   Absolute time objects typically describe a clip duration or a presentation time.
-   Frame rate objects typically describe frames to be rendered. This object includes a frame rate and frame number of the current frame. This format is used to describe [TIME\_INFO](time-info.md) parameters, and is not normally used by video transforms.

A **PIPELINE\_TIME** object that stores information in absolute time can report information in both time and frame rate. A **PIPELINE\_TIME** object that stores information in frame rate can report information only in frame rate. You can determine what type of object this is by calling its **IsFrameCount** function, which returns a Boolean value indicating whether it is a frame rate object.

The **PIPELINE\_TIME** class defines the following two data types you will use:

**REFERENCE\_TIME**

A **LONGLONG** value that describes a time in 100-nanosecond units.

**FRAMERATE**

A structure with the following syntax:

**wFrames**

The number of frames in the number of milliseconds given by **wMilliSecond**.

**wMilliSecond**

The number of milliseconds in which to present the number of frames given by **wFrames**.

The frame rate is expressed in **wFrames** frames per **wMilliSecond** milliseconds. For example, if a **FRAMERATE** had a **wFrames** value of 30 and a **wMilliSecond** value of 1000, it would be equal to 30/1000, or 30 frames per second.

To access the value in a **PIPELINE\_TIME** object, you must use the following functions.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Syntax</th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><pre data-space="preserve"><code>REFERENCE_TIME 
ToReferenceTime()</code></pre></td>
<td>Returns a time, in 100-nanosecond units.</td>
</tr>
<tr class="even">
<td><pre data-space="preserve"><code>DWORD ToMilliSecond() const </code></pre></td>
<td>Returns a time, in milliseconds.</td>
</tr>
<tr class="odd">
<td><pre data-space="preserve"><code>FRAMERATE FrameRate() const  </code></pre></td>
<td>Returns a <strong>FRAMERATE</strong> structure giving the frame rate.</td>
</tr>
<tr class="even">
<td><pre data-space="preserve"><code>bool 
IsFrameCount() const</code></pre></td>
<td>Returns a Boolean value that indicates whether this is a frame rate object. True indicates a frame rate object, and False indicates a time object.</td>
</tr>
<tr class="odd">
<td><pre data-space="preserve"><code>PIPELINE_TIME NextFrame() const</code></pre></td>
<td>Returns a <strong>PIPELINE_TIME</strong> object that represents the next frame, at the current rate.</td>
</tr>
<tr class="even">
<td><pre data-space="preserve"><code>PIPELINE_TIME PrevFrame() const</code></pre></td>
<td>Returns a <strong>PIPELINE_TIME</strong> object that represents the previous frame, at the current rate.</td>
</tr>
<tr class="odd">
<td><pre data-space="preserve"><code>int 
FrameCount() const</code></pre></td>
<td>Returns the frame number of the current object.</td>
</tr>
</tbody>
</table>



 

The **PIPELINE\_TIME** object overloads the following operators that enable you to assign, increment, decrement, and compare **PIPELINE\_TIME** objects.





 

## Requirements



|                                     |                                                                                                                             |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                                              |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                                        |
| Header<br/>                   | <dl> <dt>GPUPipelineTime.h (include Gputransformplugin.h)</dt> </dl> |



## See also

<dl> <dt>

[**Classes**](classes.md)
</dt> </dl>

 

 





