---
title: Porting Feedback Functions
description: With IRIS GL, the way that feedback is handled differs depending on the computer running IRIS GL.
ms.assetid: 170a3eae-5e0e-47f5-80dc-f8db5af98f76
keywords:
- IRIS GL porting,feedback
- porting from IRIS GL,feedback
- porting to OpenGL from IRIS GL,feedback
- OpenGL porting from IRIS GL,feedback
- feedback
ms.topic: article
ms.date: 05/31/2018
---

# Porting Feedback Functions

With IRIS GL, the way that feedback is handled differs depending on the computer running IRIS GL. OpenGL standardizes feedback functions so you can rely on consistent feedback among various hardware platforms. The following table lists the IRIS GL feedback functions and their equivalent OpenGL functions.



| IRIS GL function | OpenGL function                                                                                            | Meaning                                       |
|------------------|------------------------------------------------------------------------------------------------------------|-----------------------------------------------|
| **feedback**     | [**glRenderMode**](glrendermode.md) ( GL\_FEEDBACK )                                                      | Switches to feedback mode.                    |
| **endfeedback**  | [**glRenderMode**](glrendermode.md) ( GL\_RENDER )[**glFeedbackBuffer**](glfeedbackbuffer.md)<br/> | Switches to rendering mode.                   |
| **passthrough**  | [**glPassThrough**](glpassthrough.md)                                                                     | Places a token marker in the feedback buffer. |



 

 

 





