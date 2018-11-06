---
title: Software Shaders
description: Software shaders are implemented to allow development of shaders without underlying hardware support. They support the full feature set. Because they are implemented in software, they will not produce the best performance.
ms.assetid: 0153732d-a487-473b-ad77-32ab457979f5
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Software Shaders

Software shaders are implemented to allow development of shaders without underlying hardware support. They support the full feature set. Because they are implemented in software, they will not produce the best performance.



| Version   | Feature Set                  | Requirements                                                         |
|-----------|------------------------------|----------------------------------------------------------------------|
| vs\_2\_sw | All the features of vs\_2\_x | Only supported by software vertex processing and a reference device. |
| vs\_3\_sw | All the features of vs\_3\_0 | Only supported by software vertex processing and a reference device. |
| ps\_2\_sw | All the features of ps\_2\_x | Only supported by a reference device.                                |
| ps\_3\_sw | All the features of ps\_3\_0 | Only supported by a reference device.                                |



 

Some validations are relaxed for software shaders. This is useful for debugging and prototyping purposes. The following validations are relaxed: (all other validations remain the same)



| Validation type                                 | Relaxation                                                                                                                                                                                                          |
|-------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Instruction Counts:                             | This is relaxed for vs\_2\_sw, vs\_3\_sw and ps\_2\_sw, ps\_3\_sw. Unlimited instructions are allowed.                                                                                                              |
| Float Constant Counts:                          | This is relaxed for vs\_2\_sw, vs\_3\_sw and ps\_2\_sw, ps\_3\_sw. Up to 8192 constants are allowed.                                                                                                                |
| Integer Constant Counts:                        | This is relaxed for vs\_2\_sw, vs\_3\_sw and ps\_2\_sw, ps\_3\_sw. Up to 2048 constants are allowed.                                                                                                                |
| Boolean Constant Counts:                        | This is relaxed for vs\_2\_sw, vs\_3\_sw and ps\_2\_sw, ps\_3\_sw. Up to 2048 constants are allowed.                                                                                                                |
| Dependent-read depth:                           | This is relaxed for ps\_2\_sw. Like in vs\_3\_0 and ps\_3\_0, unlimited dependent reads are allowed.                                                                                                                |
| Number of flow control instructions and labels: | This is relaxed for vs\_2\_sw. Unlimited flow control instructions and upto 2048 labels are allowed.                                                                                                                |
| Loop count/start/step:                          | These are relaxed for vs\_2\_sw, vs\_3\_sw, ps\_2\_sw and ps\_3\_sw. Iteration start and interation step size for rep and loop instructions are 32-bit signed intergers. Interation count can be up to MAX\_INT/64. |
| Read-port limits:                               | vs\_2\_sw, vs\_3\_sw, ps\_2\_sw and ps\_3\_sw have no read-port limit.                                                                                                                                              |
| Number of interpolators:                        | There are 16 [Registers - vs\_3\_0](dx9-graphics-reference-asm-vs-registers-vs-3-0.md) (o\#) in vs\_3\_sw and 10 [ps\_3\_0 Registers](dx9-graphics-reference-asm-ps-registers-ps-3-0.md) (v\#) for ps\_3\_sw.     |



 

## Related topics

<dl> <dt>

[Asm Shader Reference](dx9-graphics-reference-asm.md)
</dt> </dl>

 

 




