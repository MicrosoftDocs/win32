---
Description: 'Specifies whether a stream associated with an IMFSensorDevice is an input or an output stream.'
ms.assetid: '598AE9EC-3B8D-419A-A6A9-02DCDD459162'
title: MFSensorStreamType enumeration
---

# MFSensorStreamType enumeration

Specifies whether a stream associated with an [**IMFSensorDevice**](imfsensordevice.md) is an input or an output stream.

## Syntax


```C++
typedef enum _MFSensorStreamType { 
  MFSensorStreamType_Unknown  = 0,
  MFSensorStreamType_Input    = 1,
  MFSensorStreamType_Output   = 2
} MFSensorStreamType;
```



## Constants

<dl> <dt>

<span id="MFSensorStreamType_Unknown"></span><span id="mfsensorstreamtype_unknown"></span><span id="MFSENSORSTREAMTYPE_UNKNOWN"></span>**MFSensorStreamType\_Unknown**
</dt> <dd>

The sensor stream type is unknown.

</dd> <dt>

<span id="MFSensorStreamType_Input"></span><span id="mfsensorstreamtype_input"></span><span id="MFSENSORSTREAMTYPE_INPUT"></span>**MFSensorStreamType\_Input**
</dt> <dd>

The sensor stream is an input stream.

</dd> <dt>

<span id="MFSensorStreamType_Output"></span><span id="mfsensorstreamtype_output"></span><span id="MFSENSORSTREAMTYPE_OUTPUT"></span>**MFSensorStreamType\_Output**
</dt> <dd>

The sensor stream is an output stream.

</dd> </dl>

 

 



