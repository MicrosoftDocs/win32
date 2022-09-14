---
title: Flow Control Nesting Limits
description: Vertex shader flow control instructions have two special restrictions.
ms.assetid: c9f80a97-8245-4974-a284-7974e2d2e504
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Flow Control Nesting Limits

Vertex shader flow control instructions have two special restrictions. Nesting depths restrict the number of instructions that can be called inside of each other. In addition, each instruction has an instruction slot count that applies against the maximum number of instruction that a shader can support.

> [!Note]  
> When you use the \*\_4\_0\_level\_9\_x HLSL shader profiles, you implicitly use of the [Shader Model 2.x](dx-graphics-hlsl-sm2.md) profiles to support Direct3D 9 capable hardware. Shader Model 2.x profiles support more limited flow control behavior than the [Shader Model 4.x](dx-graphics-hlsl-sm4.md) and later profiles.

 

## Depth Count per Instruction for vs\_2\_0

Each instruction counts against one or more nesting depth limits. This table shows the depth count that each instruction adds or subtracts from the existing depth:



| Instruction                              | Static nesting | Dynamic nesting | loop/rep nesting | call nesting | Static flow count                        |
|------------------------------------------|----------------|-----------------|------------------|--------------|------------------------------------------|
| [if bool - vs](if-bool---vs.md)         | 0              | 0               | 0                | 0            | 1                                        |
| [if\_comp - vs](if-comp---vs.md)        | n/a            | n/a             | n/a              | n/a          | n/a                                      |
| [if pred - vs](if-pred---vs.md)         | n/a            | n/a             | n/a              | n/a          | n/a                                      |
| [else - vs](else---vs.md)               | 0              | 0               | 0                | 0            | 1([if bool - vs](if-bool---vs.md) only) |
| [endif - vs](endif---vs.md)             | -1             | 0               | 0                | 0            | 0                                        |
| [rep - vs](rep---vs.md)                 | 0              | 0               | 1                | 0            | 1                                        |
| [endrep - vs](endrep---vs.md)           | 0              | 0               | -1               | 0            | 0                                        |
| [loop - vs](loop---vs.md)               | 0              | 0               | 1                | 0            | 1                                        |
| [endloop - vs](endloop---vs.md)         | 0              | 0               | -1               | 0            | 0                                        |
| [break - vs](break---vs.md)             | n/a            | n/a             | n/a              | n/a          | n/a                                      |
| [break\_comp - vs](break-comp---vs.md)  | n/a            | n/a             | n/a              | n/a          | n/a                                      |
| [breakp - vs](breakp---vs.md)           | n/a            | n/a             | n/a              | n/a          | n/a                                      |
| [call - vs](call---vs.md)               | 0              | 0               | 0                | 1            | 1                                        |
| [callnz bool - vs](callnz-bool---vs.md) | 0              | 0               | 0                | 1            | 1                                        |
| [callnz pred - vs](callnz-pred---vs.md) | n/a            | n/a             | n/a              | n/a          | n/a                                      |
| [ret - vs](ret---vs.md)                 | 0              | 0               | 0                | -1           | 0                                        |
| [setp\_comp - vs](setp-comp---vs.md)    | n/a            | n/a             | n/a              | n/a          | n/a                                      |



 

### Nesting Depth

Nesting depth define how many instructions can be called inside of each other. Each type of instruction has one or more nesting limits:



| Instruction Type  | Maximum                               |
|-------------------|---------------------------------------|
| Static nesting    | Only limited by the static flow count |
| Dynamic nesting   | n/a                                   |
| loop/rep nesting  | 1                                     |
| call nesting      | 1                                     |
| Static flow count | 16                                    |



 

## Depth Count per Instruction for vs\_2\_x

Each instruction counts against one or more nesting depth limits. This table shows the depth count that each instruction adds or subtracts from the existing depth:



| Instruction                              | Static nesting                       | Dynamic nesting                                                           | loop/rep nesting | call nesting | Static flow count                        |
|------------------------------------------|--------------------------------------|---------------------------------------------------------------------------|------------------|--------------|------------------------------------------|
| [if bool - vs](if-bool---vs.md)         | 1                                    | 0                                                                         | 0                | 0            | 1                                        |
| [if\_comp - vs](if-comp---vs.md)        | 0                                    | 1                                                                         | 0                | 0            | 0                                        |
| [if pred - vs](if-pred---vs.md)         | 0                                    | 1                                                                         | 0                | 0            | 0                                        |
| [else - vs](else---vs.md)               | 0                                    | 0                                                                         | 0                | 0            | 1([if bool - vs](if-bool---vs.md) only) |
| [endif - vs](endif---vs.md)             | -1([if bool - vs](if-bool---vs.md)) | -1([if pred - vs](if-pred---vs.md) or [if\_comp - vs](if-comp---vs.md)) | 0                | 0            | 0                                        |
| [rep - vs](rep---vs.md)                 | 0                                    | 0                                                                         | 1                | 0            | 1                                        |
| [endrep - vs](endrep---vs.md)           | 0                                    | 0                                                                         | -1               | 0            | 0                                        |
| [loop - vs](loop---vs.md)               | 0                                    | 0                                                                         | 1                | 0            | 1                                        |
| [endloop - vs](endloop---vs.md)         | 0                                    | 0                                                                         | -1               | 0            | 0                                        |
| [break - vs](break---vs.md)             | 0                                    | 0                                                                         | 0                | 0            | 0                                        |
| [break\_comp - vs](break-comp---vs.md)  | 0                                    | 1, -1                                                                     | 0                | 0            | 0                                        |
| [breakp - vs](breakp---vs.md)           | 0                                    | 0                                                                         | 0                | 0            | 0                                        |
| [call - vs](call---vs.md)               | 0                                    | 0                                                                         | 0                | 1            | 1                                        |
| [callnz bool - vs](callnz-bool---vs.md) | 0                                    | 0                                                                         | 0                | 1            | 1                                        |
| [callnz pred - vs](callnz-pred---vs.md) | 0                                    | 1                                                                         | 0                | 1            | 0                                        |
| [ret - vs](ret---vs.md)                 | 0                                    | -1 ([callnz pred - vs](callnz-pred---vs.md))                             | 0                | -1           | 0                                        |
| [setp\_comp - vs](setp-comp---vs.md)    | 0                                    | 0                                                                         | 0                | 0            | 0                                        |



 

### Nesting Depth

Nesting depth define how many instructions can be called inside of each other. Each type of instruction has one or more nesting limits:



| Instruction Type  | Maximum                                                                              |
|-------------------|--------------------------------------------------------------------------------------|
| Static nesting    | Only limited by the static flow count                                                |
| Dynamic nesting   | 0 or 24, see D3DCAPS9.VS20Caps.DynamicFlowControlDepth                               |
| loop/rep nesting  | 1 to 4, see D3DCAPS9.VS20Caps.StaticFlowControlDepth                                 |
| call nesting      | 1 to 4, see D3DCAPS9.VS20Caps.StaticFlowControlDepth (independent of loop/rep limit) |
| Static flow count | 16                                                                                   |



 

## Depth Count per Instruction for vs\_2\_sw

Each instruction counts against one or more nesting depth limits. This table shows the depth count that each instruction adds or subtracts from the existing depth:



| Instruction                              | Static nesting                       | Dynamic nesting                                                           | loop/rep nesting | call nesting | Static flow count |
|------------------------------------------|--------------------------------------|---------------------------------------------------------------------------|------------------|--------------|-------------------|
| [if bool - vs](if-bool---vs.md)         | 1                                    | 0                                                                         | 0                | 0            | n/a               |
| [if\_comp - vs](if-comp---vs.md)        | 0                                    | 1                                                                         | 0                | 0            | n/a               |
| [if pred - vs](if-pred---vs.md)         | 0                                    | 1                                                                         | 0                | 0            | n/a               |
| [else - vs](else---vs.md)               | 0                                    | 0                                                                         | 0                | 0            | n/a               |
| [endif - vs](endif---vs.md)             | -1([if bool - vs](if-bool---vs.md)) | -1([if pred - vs](if-pred---vs.md) or [if\_comp - vs](if-comp---vs.md)) | 0                | 0            | n/a               |
| [rep - vs](rep---vs.md)                 | 0                                    | 0                                                                         | 1                | 0            | n/a               |
| [endrep - vs](endrep---vs.md)           | 0                                    | 0                                                                         | -1               | 0            | n/a               |
| [loop - vs](loop---vs.md)               | 0                                    | 0                                                                         | 1                | 0            | n/a               |
| [endloop - vs](endloop---vs.md)         | 0                                    | 0                                                                         | -1               | 0            | n/a               |
| [break - vs](break---vs.md)             | 0                                    | 0                                                                         | 0                | 0            | n/a               |
| [break\_comp - vs](break-comp---vs.md)  | 0                                    | 1, -1                                                                     | 0                | 0            | n/a               |
| [breakp - vs](breakp---vs.md)           | 0                                    | 0                                                                         | 0                | 0            | n/a               |
| [call - vs](call---vs.md)               | 0                                    | 0                                                                         | 0                | 1            | n/a               |
| [callnz bool - vs](callnz-bool---vs.md) | 0                                    | 0                                                                         | 0                | 1            | n/a               |
| [callnz pred - vs](callnz-pred---vs.md) | 0                                    | 1                                                                         | 0                | 1            | n/a               |
| [ret - vs](ret---vs.md)                 | 0                                    | -1 ([callnz pred - vs](callnz-pred---vs.md))                             | 0                | -1           | n/a               |
| [setp\_comp - vs](setp-comp---vs.md)    | 0                                    | 0                                                                         | 0                | 0            | n/a               |



 

### Nesting Depth

Nesting depth define how many instructions can be called inside of each other. Each type of instruction has one or more nesting limits:



| Instruction Type  | Maximum  |
|-------------------|----------|
| Static nesting    | 24       |
| Dynamic nesting   | 24       |
| loop/rep nesting  | 4        |
| call nesting      | 4        |
| Static flow count | No limit |



 

## Depth Count per Instruction for vs\_3\_0

Each instruction counts against one or more nesting depth limits. This table shows the depth count that each instruction adds or subtracts from the existing depth:



| Instruction                              | Static nesting                       | Dynamic nesting                                                           | loop/rep nesting | call nesting | Static flow count |
|------------------------------------------|--------------------------------------|---------------------------------------------------------------------------|------------------|--------------|-------------------|
| [if bool - vs](if-bool---vs.md)         | 1                                    | 0                                                                         | 0                | 0            | n/a               |
| [if\_comp - vs](if-comp---vs.md)        | 0                                    | 1                                                                         | 0                | 0            | n/a               |
| [if pred - vs](if-pred---vs.md)         | 0                                    | 1                                                                         | 0                | 0            | n/a               |
| [else - vs](else---vs.md)               | 0                                    | 0                                                                         | 0                | 0            | n/a               |
| [endif - vs](endif---vs.md)             | -1([if bool - vs](if-bool---vs.md)) | -1([if pred - vs](if-pred---vs.md) or [if\_comp - vs](if-comp---vs.md)) | 0                | 0            | n/a               |
| [rep - vs](rep---vs.md)                 | 0                                    | 0                                                                         | 1                | 0            | n/a               |
| [endrep - vs](endrep---vs.md)           | 0                                    | 0                                                                         | -1               | 0            | n/a               |
| [loop - vs](loop---vs.md)               | 0                                    | 0                                                                         | 1                | 0            | n/a               |
| [endloop - vs](endloop---vs.md)         | 0                                    | 0                                                                         | -1               | 0            | n/a               |
| [break - vs](break---vs.md)             | 0                                    | 0                                                                         | 0                | 0            | n/a               |
| [break\_comp - vs](break-comp---vs.md)  | 0                                    | 1, -1                                                                     | 0                | 0            | n/a               |
| [breakp - vs](breakp---vs.md)           | 0                                    | 0                                                                         | 0                | 0            | n/a               |
| [call - vs](call---vs.md)               | 0                                    | 0                                                                         | 0                | 1            | n/a               |
| [callnz bool - vs](callnz-bool---vs.md) | 0                                    | 0                                                                         | 0                | 1            | n/a               |
| [callnz pred - vs](callnz-pred---vs.md) | 0                                    | 1                                                                         | 0                | 1            | n/a               |
| [ret - vs](ret---vs.md)                 | 0                                    | -1 ([callnz pred - vs](callnz-pred---vs.md))                             | 0                | -1           | n/a               |
| [setp\_comp - vs](setp-comp---vs.md)    | 0                                    | 0                                                                         | 0                | 0            | n/a               |



 

### Nesting Depth

Nesting depth define how many instructions can be called inside of each other. Each type of instruction has one or more nesting limits:



| Instruction Type  | Maximum  |
|-------------------|----------|
| Static nesting    | 24       |
| Dynamic nesting   | 24       |
| loop/rep nesting  | 4        |
| call nesting      | 4        |
| Static flow count | No limit |



 

## Depth Count per Instruction for vs\_3\_sw

Each instruction counts against one or more nesting depth limits. This table shows the depth count that each instruction adds or subtracts from the existing depth:



| Instruction                              | Static nesting                       | Dynamic nesting                                                           | loop/rep nesting | call nesting | Static flow count |
|------------------------------------------|--------------------------------------|---------------------------------------------------------------------------|------------------|--------------|-------------------|
| [if bool - vs](if-bool---vs.md)         | 1                                    | 0                                                                         | 0                | 0            | n/a               |
| [if\_comp - vs](if-comp---vs.md)        | 0                                    | 1                                                                         | 0                | 0            | n/a               |
| [if pred - vs](if-pred---vs.md)         | 0                                    | 1                                                                         | 0                | 0            | n/a               |
| [else - vs](else---vs.md)               | 0                                    | 0                                                                         | 0                | 0            | n/a               |
| [endif - vs](endif---vs.md)             | -1([if bool - vs](if-bool---vs.md)) | -1([if pred - vs](if-pred---vs.md) or [if\_comp - vs](if-comp---vs.md)) | 0                | 0            | n/a               |
| [rep - vs](rep---vs.md)                 | 0                                    | 0                                                                         | 1                | 0            | n/a               |
| [endrep - vs](endrep---vs.md)           | 0                                    | 0                                                                         | -1               | 0            | n/a               |
| [loop - vs](loop---vs.md)               | 0                                    | 0                                                                         | 1                | 0            | n/a               |
| [endloop - vs](endloop---vs.md)         | 0                                    | 0                                                                         | -1               | 0            | n/a               |
| [break - vs](break---vs.md)             | 0                                    | 0                                                                         | 0                | 0            | n/a               |
| [break\_comp - vs](break-comp---vs.md)  | 0                                    | 1, -1                                                                     | 0                | 0            | n/a               |
| [breakp - vs](breakp---vs.md)           | 0                                    | 0                                                                         | 0                | 0            | n/a               |
| [call - vs](call---vs.md)               | 0                                    | 0                                                                         | 0                | 1            | n/a               |
| [callnz bool - vs](callnz-bool---vs.md) | 0                                    | 0                                                                         | 0                | 1            | n/a               |
| [callnz pred - vs](callnz-pred---vs.md) | 0                                    | 1                                                                         | 0                | 1            | n/a               |
| [ret - vs](ret---vs.md)                 | 0                                    | -1 ([callnz pred - vs](callnz-pred---vs.md))                             | 0                | -1           | n/a               |
| [setp\_comp - vs](setp-comp---vs.md)    | 0                                    | 0                                                                         | 0                | 0            | n/a               |



 

### Nesting Depth

Nesting depth define how many instructions can be called inside of each other. Each type of instruction has one or more nesting limits:



| Instruction Type  | Maximum  |
|-------------------|----------|
| Static nesting    | 24       |
| Dynamic nesting   | 24       |
| loop/rep nesting  | 4        |
| call nesting      | 4        |
| Static flow count | No limit |



 

## Related topics

<dl> <dt>

[Vertex Shader Instructions](dx9-graphics-reference-asm-vs-instructions.md)
</dt> </dl>

 

 




