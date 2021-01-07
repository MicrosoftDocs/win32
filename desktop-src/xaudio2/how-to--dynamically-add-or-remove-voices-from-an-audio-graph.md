---
description: You can change audio graphs at any time to add or remove voices or entire subgraphs.
ms.assetid: b2f9ec6a-4b5b-e618-759b-d7dbc0d97ac4
title: 'How to: Dynamically Add or Remove Voices From an Audio Graph'
ms.topic: article
ms.date: 05/31/2018
---

# How to: Dynamically Add or Remove Voices From an Audio Graph

You can change audio graphs at any time to add or remove voices or entire subgraphs. This topic shows you how to add or remove submix voices from a graph that has been created following the steps in [How to: Build a Basic Audio Processing Graph](how-to--build-a-basic-audio-processing-graph.md). A single voice can send its output to several voices or to a long chain of voices. Removing or adding a single voice can have a large effect on an audio graph.

## To dynamically change an audio graph

Adding and removing voices from an audio graph is very similar to adding or removing nodes from a single-linked list or graph.

-   To add a voice or subgraph to an audio graph

    Set the output of a voice in the graph, the parent voice, to the voice to be added using the [**SetOutputVoices**](/windows/win32/api/xaudio2/nf-xaudio2-ixaudio2voice-setoutputvoices) function. Set the output of the new voice to the original child of the parent voice.

    ```
    XAUDIO2_SEND_DESCRIPTOR send = {0, pNewVoice};
    XAUDIO2_VOICE_SENDS sendlist = {1, &send};
    pParentVoice->SetOutputVoices(&sendlist);
    send.pOutputVoice = pChildVoice;
    pNewVoice->SetOutputVoices(&sendlist);
    ```

    

-   To remove a voice or subgraph from an audio graph

    Set the output voice of the parent of the voice being removed to the child of the voice being removed. If the voice being removed is at the end of the graph, the parent voice should be changed to point to the master voice.

    ```
    XAUDIO2_SEND_DESCRIPTOR send = {0, pChildVoice};
    XAUDIO2_VOICE_SENDS sendlist = {1, &send};
    pParentVoice->SetOutputVoices(&sendlist);
    ```

    

Note that for clarity each parent only has one child in these examples. If a parent node has multiple children, its sendlist will contain an array of voices instead of a pointer to just one voice.

## Related topics

<dl> <dt>

[Audio Graphs](audio-graphs.md)
</dt> <dt>

[XAudio2 Programming Guide](programming-guide.md)
</dt> <dt>

[How to: Build a Basic Audio Processing Graph](how-to--build-a-basic-audio-processing-graph.md)
</dt> <dt>

[How to: Use Submix Voices](how-to--use-submix-voices.md)
</dt> <dt>

[How to: Create an Effect Chain](how-to--create-an-effect-chain.md)
</dt> </dl>

 

 
