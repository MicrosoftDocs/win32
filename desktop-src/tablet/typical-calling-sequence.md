---
description: The methods you must implement to create an ink recognizer are called by the Tablet PC Platform APIs and not directly by an ink-enabled application.The following steps represent a typical calling sequence for the implementation of these methods:The DLL is loaded.An&\#160;HRECOGNIZER handle is created.An&\#160;HRECOCONTEXT handle is created.Recognizer options and modes are set for this context.Strokes are added to the ink data.Input is ended.The ink is recognized.The recognition results are returned.The HRECOCONTEXT handle is destroyed.The HRECOGNIZER handle is destroyed.The calling sequence is also illustrated in the following code outline:C++CreateRecognizer(CLSID, &hrec); while (more pieces of ink to recognize ... ) { // Create a context, once per piece of ink to be recognized hrc = CreateContext(hrec, &hrc); // Functions to set up options and modes for this context SetGuide(hrc, pGuide, 0); SetFactoid(hrc, 5, PHONE); // only if in application with forms SetFlags(hrc, RECOFLAG\_WORDMODE); // rare, only if wanting word mode, no out-of-dictionary, or single segmentation SetWordList(hrc, hwl); // Adding all the strokes in this piece of ink while (more strokes ... ) { AddStroke(hrc, NULL, 800, pPacket, pXForm); // one call per stroke } EndInkInput(hrc); // This gets the ink recognized Process(hrc); // If this is a simple application, it calls this for a simple answer GetBestResultString(hrc, length, buffer); // If this is a complex application, it calls this for a complete answer GetLatticePtr(hrc, &pLattice); // Destroy the context DestroyContext(hrc); } // Called just before the application shuts down DestroyRecognizer(hrec);
ms.assetid: 484ba140-788f-4b71-9cc7-9baa919d9936
title: Typical Calling Sequence
ms.topic: article
ms.date: 05/31/2018
---

# Typical Calling Sequence

The methods you must implement to create an ink recognizer are called by the Tablet PC Platform APIs and not directly by an ink-enabled application.

The following steps represent a typical calling sequence for the implementation of these methods:

1.  The DLL is loaded.
2.  An [HRECOGNIZER](hrecognizer-handle.md) handle is created.
3.  An [HRECOCONTEXT](hrecocontext-handle.md) handle is created.
4.  Recognizer options and modes are set for this context.
5.  Strokes are added to the ink data.
6.  Input is ended.
7.  The ink is recognized.
8.  The recognition results are returned.
9.  The [HRECOCONTEXT](hrecocontext-handle.md) handle is destroyed.
10. The [HRECOGNIZER](hrecognizer-handle.md) handle is destroyed.

The calling sequence is also illustrated in the following code outline:


```C++
CreateRecognizer(CLSID, &hrec);
while (more pieces of ink to recognize ... )
{
  // Create a context, once per piece of ink to be recognized
  hrc = CreateContext(hrec, &hrc);

  // Functions to set up options and modes for this context
  SetGuide(hrc, pGuide, 0);
  SetFactoid(hrc, 5, PHONE); // only if in application with forms
  SetFlags(hrc, RECOFLAG_WORDMODE); // rare, only if wanting word mode, no out-of-dictionary, or single segmentation
  SetWordList(hrc, hwl);

  // Adding all the strokes in this piece of ink
  while (more strokes ... )
  {
    AddStroke(hrc, NULL, 800, pPacket, pXForm);  // one call per stroke
  }
  EndInkInput(hrc);

  // This gets the ink recognized
  Process(hrc);

  // If this is a simple application, it calls this for a simple answer
  GetBestResultString(hrc, length, buffer);

  // If this is a complex application, it calls this for a complete answer
  GetLatticePtr(hrc, &pLattice);

  // Destroy the context
  DestroyContext(hrc);
}
// Called just before the application shuts down
DestroyRecognizer(hrec);
```



## Related topics

<dl> <dt>

[Recognizer APIs](recognizer-apis.md)
</dt> <dt>

[Recognition API Architecture](recognition-api-architecture.md)
</dt> </dl>

 

 



