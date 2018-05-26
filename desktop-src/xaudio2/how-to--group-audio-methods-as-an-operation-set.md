---
Description: This topic shows you how you can group together XAudio2 methods so they take effect at the same time.
ms.assetid: 1b50acc5-a6b2-e010-9e7e-0080a5ee4a58
title: How to Group Audio Methods as an Operation Set
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# How to: Group Audio Methods as an Operation Set

This topic shows you how you can group together XAudio2 methods so they take effect at the same time.

## To group audio methods as an operation set

1.  Declare a global operation set counter.

    The [operation set](operation-sets.md) counter ensures that each operation set is unique.

    ```
    UINT32 OperationSetCounter = 0;
    ```

    

2.  Increment the global counter.

    Each time you submit a new [operation set](operation-sets.md), the global counter should increment to ensure each set is unique.

    ```
    UINT32 OperationID = UINT32(InterlockedIncrement(LPLONG(&amp;OperationSetCounter)));
    ```

    

3.  Group the method calls by setting their [operation set](operation-sets.md) parameters.

4.  Set the [operation set](operation-sets.md) parameters to the current value of the global counter.

    In this case, four calls to [**IXAudio2SourceVoice::Start**](ixaudio2sourcevoice-interface-start.md) are grouped as one [operation set](operation-sets.md). Grouping the calls causes all four of the sounds to start at exactly the same time.

    ```
    hr = pSFXSourceVoice1->Start( 0, OperationID );
    hr = pSFXSourceVoice2->Start( 0, OperationID );
    hr = pSFXSourceVoice3->Start( 0, OperationID );
    hr = pSFXSourceVoice4->Start( 0, OperationID );
    ```

    

5.  Start the [operation set](operation-sets.md).

    After you call all the methods in the set, start the set by calling [**IXAudio2::CommitChanges**](ixaudio2-interface-commitchanges.md) with the current value of the global counter.

    ```
    pXAudio2->CommitChanges(OperationID);
    ```

    

## Related topics

<dl> <dt>

[Operation Sets](operation-sets.md)
</dt> <dt>

[XAudio2 Programming Guide](programming-guide.md)
</dt> <dt>

[XAudio2 Operation Sets](xaudio2-operation-sets.md)
</dt> </dl>

 

 



