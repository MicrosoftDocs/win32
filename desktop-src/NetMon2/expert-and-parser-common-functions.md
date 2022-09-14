---
description: The Network Monitor functions, listed in the following table, can be used to develop either parsers or experts.
ms.assetid: 26eb4f99-a8dc-43a2-abb9-9577518b6f2f
title: Expert and Parser Common Functions
ms.topic: article
ms.date: 05/31/2018
---

# Expert and Parser Common Functions

The Network Monitor functions, listed in the following table, can be used to develop either [*parsers*](p.md) or [*experts*](e.md).



| Function                                                               | Description                                                                         |
|------------------------------------------------------------------------|-------------------------------------------------------------------------------------|
| [CompareAddresses](compareaddresses.md)                               | Compares two given addresses.                                                       |
| [CompareFrameDestAddress](compareframedestaddress.md)                 | Compares a given address to the destination address of a frame.                     |
| [CompareFrameSourceAddress](compareframesourceaddress.md)             | Compares a given address to the source address of a frame.                          |
| [FilterAddObject](filteraddobject.md)                                 | Adds a single object to a filter.                                                   |
| [FindPropertyInstance](findpropertyinstance.md)                       | Finds the first instance of a given property.                                       |
| [FindPropertyInstanceRestart](findpropertyinstancerestart.md)         | Finds the next instance of a given property.                                        |
| [GetCaptureComment](getcapturecomment.md)                             | Retrieves the comment of a capture.                                                 |
| [GetCaptureCommentFromFilename](getcapturecommentfromfilename.md)     | Retrieves the comment of a capture from its capture file.                           |
| [GetCaptureMacType](getcapturemactype.md)                             | Retrieves the MAC type of the capture.                                              |
| [GetCaptureTimeStamp](getcapturetimestamp.md)                         | Retrieves the capture timeout stamp.                                                |
| [GetCaptureTotalFrames](getcapturetotalframes.md)                     | Retrieves the total frames in the capture.                                          |
| [GetEnabledProtocols](getenabledprotocols.md)                         | Retrieves a list of all the protocols marked as enabled.                            |
| [GetFrame](getframe.md)                                               | Retrieves a handle to a given frame.                                                |
| [GetFrameCaptureHandle](getframecapturehandle.md)                     | Retrieves a handle to a given capture.                                              |
| [GetFrameDstAddressOffset](getframedstaddressoffset.md)               | Retrieves the destination address offset for a given frame.                         |
| [GetFrameFromFrameHandle](getframefromframehandle.md)                 | Retrieves a frame for a given frame handle.                                         |
| [GetFrameLength](getframelength.md)                                   | Retrieves the length of a given frame.                                              |
| [GetFrameMacHeaderLength](getframemacheaderlength.md)                 | Retrieves the length of the MAC header for a given frame.                           |
| [GetFrameMacType](getframemactype.md)                                 | Retrieves the MAC type for a given frame.                                           |
| [GetFrameNumber](getframenumber.md)                                   | Returns the number of a given frame.                                                |
| [GetFrameRecognizeData](getframerecognizedata.md)                     | Retrieves the protocol identifiers (and their offsets) of all recognized protocols. |
| [GetFrameSrcAddressOffset](getframesrcaddressoffset.md)               | Retrieves the offset to the source address of a given frame.                        |
| [GetFrameStoredLength](getframestoredlength.md)                       | Retrieves the length of a given frame.                                              |
| [GetFrameTimeStamp](getframetimestamp.md)                             | Retrieves the time stamp of a given frame.                                          |
| [GetPreviousProtocolOffsetByName](getpreviousprotocoloffsetbyname.md) | Retrieves the previous instance of a given protocol.                                |
| [GetProperty](getproperty.md)                                         | Retrieves a property with a given name.                                             |
| [GetPropertyInfo](getpropertyinfo.md)                                 | Retrieves the information of a specific property.                                   |
| [GetPropertyText](getpropertytext.md)                                 | Retrieves the text of a given property.                                             |
| [GetProtocolFromName](getprotocolfromname.md)                         | Retrieves a specific protocol by name.                                              |
| [GetProtocolInfo](getprotocolinfo.md)                                 | Uses the protocol handle to retrieves protocol-related data.                        |
| [GetProtocolStartOffsetHandle](getprotocolstartoffsethandle.md)       | Retrieves the offset of a given protocol.                                           |
| [MacTypeToAddressType](mactypetoaddresstype.md)                       | Converts a MAC type to an address type.                                             |
| [ModifyFrame](modifyframe.md)                                         | Updates an existing frame with new data.                                            |



 

For more information about functions and structures only used by experts, and functions and structures only used by parsers, see the topics listed in the following table.



| For more information about                                          | See                                                                                                |
|---------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|
| Expert-specific functions that you can used to develop expert DLLs. | [Expert Functions, Structures, and Enumerations](expert-functions-structures-and-enumerations.md) |
| Parser-specific functions that you can used to develop parser DLLs. | [Parser Functions and Structures](parser-functions-and-structures.md)                             |



 

 

 



