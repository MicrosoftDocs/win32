---
Description: 'The EXpsJobConsumption enumeration describes job consumption updates.'
ms.assetid: '9fab1cba-fe67-4654-ae33-3de41f0427f7'
title: EXpsJobConsumption enumeration
---

# EXpsJobConsumption enumeration

The EXpsJobConsumption enumeration describes job consumption updates.

## Syntax


```C++
typedef enum  { 
  XpsJob_DocumentSequenceAdded,
  XpsJob_FixedDocumentAdded,
  XpsJob_FixedPageAdded
} EXpsJobConsumption;
```



## Constants

<dl> <dt>

<span id="XpsJob_DocumentSequenceAdded"></span><span id="xpsjob_documentsequenceadded"></span><span id="XPSJOB_DOCUMENTSEQUENCEADDED"></span>**XpsJob\_DocumentSequenceAdded**
</dt> <dd>

A document sequence is added to the job.

</dd> <dt>

<span id="XpsJob_FixedDocumentAdded"></span><span id="xpsjob_fixeddocumentadded"></span><span id="XPSJOB_FIXEDDOCUMENTADDED"></span>**XpsJob\_FixedDocumentAdded**
</dt> <dd>

A fixed document is added to the job.

</dd> <dt>

<span id="XpsJob_FixedPageAdded"></span><span id="xpsjob_fixedpageadded"></span><span id="XPSJOB_FIXEDPAGEADDED"></span>**XpsJob\_FixedPageAdded**
</dt> <dd>

A fixed page is added to the job.

</dd> </dl>

## Remarks

A rendering filter uses the [IPrintPipelineProgressReport](iprintpipelineprogressreport.md) interface to send updates to the pipeline.

Rendering filters convert XPS to the page description language (PDL).

A pipeline does not necessarily need one of the EXpsJobConsumption enumeration values.

## Requirements



|                   |                                                                                                                        |
|-------------------|------------------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Filterpipeline.h (include Filterpipeline.h)</dt> </dl> |
| IDL<br/>    | <dl> <dt>Filterpipeline.idl</dt> </dl>                          |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20EXpsJobConsumption%20enumeration%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




