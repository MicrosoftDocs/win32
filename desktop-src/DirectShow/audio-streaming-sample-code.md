---
description: Audio Streaming Sample Code
ms.assetid: f3ba32c5-c3de-4f6b-bc89-f7860ca5f65b
title: Audio Streaming Sample Code
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Audio Streaming Sample Code

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> These APIs are deprecated. Applications should use the [**Sample Grabber**](sample-grabber-filter.md) filter or implement a custom filter to get data from a DirectShow filter graph.

 

The following code sample demonstrates how to stream audio data using the [**IAudioMediaStream**](/previous-versions/windows/desktop/api/austream/nn-austream-iaudiomediastream), [**IAudioStreamSample**](/previous-versions/windows/desktop/api/austream/nn-austream-iaudiostreamsample), [**IMemoryData**](/previous-versions/windows/desktop/api/austream/nn-austream-imemorydata), and [**IAudioData**](/previous-versions/windows/desktop/api/austream/nn-austream-iaudiodata) interfaces. For brevity, this example performs minimal error checking.


```C++
#include <windows.h>
#include <stdio.h>
#include <mmsystem.h>
#include <amstream.h>

class CWaveBuffer {
    public:
        ~CWaveBuffer();
        BOOL Init(HWAVEOUT hWave, int Size);
        BOOL Write(PBYTE pData, int nBytes, int& BytesWritten);
        void Flush();
    private:
        WAVEHDR      m_Hdr;
        HWAVEOUT     m_hWave;
        int          m_nBytes;
};

class CWaveOut {
    public:
        CWaveOut(LPCWAVEFORMATEX Format, int nBuffers, int BufferSize);
        ~CWaveOut();
        void Write(PBYTE Data, int nBytes);
        void Flush();
        void Wait();
        void Reset();
    private:
        const HANDLE   m_hSem;
        const int      m_nBuffers;
        int            m_CurrentBuffer;
        BOOL           m_NoBuffer;
        CWaveBuffer   *m_Hdrs;
        HWAVEOUT       m_hWave;
};

BOOL CWaveBuffer::Init(HWAVEOUT hWave, int Size)
{
    m_hWave  = hWave;
    m_nBytes = 0;

    /*  Allocate a buffer and initialize the header. */
    m_Hdr.lpData = (LPSTR)LocalAlloc(LMEM_FIXED, Size);
    if (m_Hdr.lpData == NULL) 
    {
        return FALSE;
    }
    m_Hdr.dwBufferLength  = Size;
    m_Hdr.dwBytesRecorded = 0;
    m_Hdr.dwUser = 0;
    m_Hdr.dwFlags = 0;
    m_Hdr.dwLoops = 0;
    m_Hdr.lpNext = 0;
    m_Hdr.reserved = 0;

    /*  Prepare it. */
    waveOutPrepareHeader(hWave, &m_Hdr, sizeof(WAVEHDR));
    return TRUE;
}

CWaveBuffer::~CWaveBuffer() 
{
    if (m_Hdr.lpData) 
    {
        waveOutUnprepareHeader(m_hWave, &m_Hdr, sizeof(WAVEHDR));
        LocalFree(m_Hdr.lpData);
    }
}

void CWaveBuffer::Flush()
{
    // ASSERT(m_nBytes != 0);
    m_nBytes = 0;
    waveOutWrite(m_hWave, &m_Hdr, sizeof(WAVEHDR));
}

BOOL CWaveBuffer::Write(PBYTE pData, int nBytes, int& BytesWritten)
{
    // ASSERT((DWORD)m_nBytes != m_Hdr.dwBufferLength);
    BytesWritten = min((int)m_Hdr.dwBufferLength - m_nBytes, nBytes);
    CopyMemory((PVOID)(m_Hdr.lpData + m_nBytes), (PVOID)pData, BytesWritten);
    m_nBytes += BytesWritten;
    if (m_nBytes == (int)m_Hdr.dwBufferLength) 
    {
        /*  Write it! */
        m_nBytes = 0;
        waveOutWrite(m_hWave, &m_Hdr, sizeof(WAVEHDR));
        return TRUE;
    }
    return FALSE;
}

void CALLBACK WaveCallback(HWAVEOUT hWave, UINT uMsg, DWORD dwUser, 
                           DWORD dw1, DWORD dw2)
{
    if (uMsg == WOM_DONE) 
    {
        ReleaseSemaphore((HANDLE)dwUser, 1, NULL);
    }
}

CWaveOut::CWaveOut(LPCWAVEFORMATEX Format, int nBuffers, int BufferSize) :
    m_nBuffers(nBuffers),
    m_CurrentBuffer(0),
    m_NoBuffer(TRUE),
    m_hSem(CreateSemaphore(NULL, nBuffers, nBuffers, NULL)),
    m_Hdrs(new CWaveBuffer[nBuffers]),
    m_hWave(NULL)
{
    /*  Create wave device. */
    waveOutOpen(&m_hWave,
                WAVE_MAPPER,
                Format,
                (DWORD)WaveCallback,
                (DWORD)m_hSem,
                CALLBACK_FUNCTION);

    /*  Initialize the wave buffers. */
    for (int i = 0; i < nBuffers; i++) 
    {
        m_Hdrs[i].Init(m_hWave, BufferSize);
    }
}

CWaveOut::~CWaveOut()
{
    /*  First, get the buffers back. */
    waveOutReset(m_hWave);
    /*  Free the buffers. */
    delete [] m_Hdrs;
    /*  Close the wave device. */
    waveOutClose(m_hWave);
    /*  Free the semaphore. */
    CloseHandle(m_hSem);
}

void CWaveOut::Flush()
{
    if (!m_NoBuffer) 
    {
        m_Hdrs[m_CurrentBuffer].Flush();
        m_NoBuffer = TRUE;
        m_CurrentBuffer = (m_CurrentBuffer + 1) % m_nBuffers;
    }
}

void CWaveOut::Reset()
{
    waveOutReset(m_hWave);
}

void CWaveOut::Write(PBYTE pData, int nBytes)
{
    while (nBytes != 0) 
    {
        /*  Get a buffer if necessary. */
        if (m_NoBuffer) 
        {
            WaitForSingleObject(m_hSem, INFINITE);
            m_NoBuffer = FALSE;
        }

        /*  Write into a buffer. */
        int nWritten;
        if (m_Hdrs[m_CurrentBuffer].Write(pData, nBytes, nWritten)) 
        {
            m_NoBuffer = TRUE;
            m_CurrentBuffer = (m_CurrentBuffer + 1) % m_nBuffers;
            nBytes -= nWritten;
            pData += nWritten;
        } 
        else 
        {
            // ASSERT(nWritten == nBytes);
            break;
        }
    }
}

void CWaveOut::Wait()
{
    /*  Send any remaining buffers. */
    Flush();
    /*  Wait for the buffers back. */
    for (int i = 0; i < m_nBuffers; i++) 
    {
        WaitForSingleObject(m_hSem, INFINITE);
    }
    LONG lPrevCount;
    ReleaseSemaphore(m_hSem, m_nBuffers, &lPrevCount);
}

HRESULT RenderStreamToDevice(IMultiMediaStream *pMMStream)
{
    WAVEFORMATEX wfx;
    #define DATA_SIZE 5000

    IMediaStream        *pStream = NULL;
    IAudioStreamSample  *pSample = NULL;
    IAudioMediaStream   *pAudioStream = NULL;
    IAudioData          *pAudioData = NULL;

    HRESULT hr = pMMStream->GetMediaStream(MSPID_PrimaryAudio, &pStream);
    if (FAILED(hr))
    {
        return hr;
    }

    pStream->QueryInterface(IID_IAudioMediaStream, (void **)&pAudioStream);
    pStream->Release();

    hr = CoCreateInstance(CLSID_AMAudioData, NULL, 
        CLSCTX_INPROC_SERVER, IID_IAudioData, (void **)&pAudioData);
    if (FAILED(hr))
    {
        pAudioStream->Release();
        return hr;
    }

    PBYTE pBuffer = (PBYTE)LocalAlloc(LMEM_FIXED, DATA_SIZE);
    if (pBuffer == NULL)
    {
        pAudioStream->Release();
        pAudioData->Release();
        return E_OUTOFMEMORY;
    }

    pAudioStream->GetFormat(&wfx);
    pAudioData->SetBuffer(DATA_SIZE, pBuffer, 0);
    pAudioData->SetFormat(&wfx);
    hr = pAudioStream->CreateSample(pAudioData, 0, &pSample);
    pAudioStream->Release();
    if (FAILED(hr))
    {
        LocalFree((HLOCAL)pBuffer);
        pAudioData->Release();
        pSample->Release();
        return hr;
    }

    CWaveOut WaveOut(&wfx, 4, 2048);
    HANDLE hEvent = CreateEvent(FALSE, NULL, NULL, FALSE);
    if (hEvent != 0)
    {
        int iTimes;
        for (iTimes = 0; iTimes < 3; iTimes++) 
        {
            DWORD dwStart = timeGetTime();
            for (; ; ) 
            {
                hr = pSample->Update(0, hEvent, NULL, 0);
                if (FAILED(hr) || hr == MS_S_ENDOFSTREAM) 
                {
                    break;
                }
                WaitForSingleObject(hEvent, INFINITE);
                DWORD dwTimeDiff = timeGetTime() - dwStart;
                // Limit to 10 seconds
                if (dwTimeDiff > 10000) {
                    break;
                }
                DWORD dwLength;
                pAudioData->GetInfo(NULL, NULL, &dwLength);
                WaveOut.Write(pBuffer, dwLength);
            }
            pMMStream->Seek(0);
        }
    }

    pAudioData->Release();
    pSample->Release();
    LocalFree((HLOCAL)pBuffer);
    return S_OK;
}

HRESULT RenderFileToMMStream(
    const char * szFileName, 
    IMultiMediaStream **ppMMStream)
{
    if (strlen(szFileName) > MAX_PATH)
    {
        return E_INVALIDARG;
    }

    IAMMultiMediaStream *pAMStream;
    HRESULT hr = CoCreateInstance(CLSID_AMMultiMediaStream, NULL, 
        CLSCTX_INPROC_SERVER, IID_IAMMultiMediaStream, 
        (void **)&pAMStream);
    if (FAILED(hr))
    { 
        return hr;
    }

    WCHAR wszName[MAX_PATH + 1];
    MultiByteToWideChar(CP_ACP, 0, szFileName, -1, wszName,
        MAX_PATH + 1);
    
    pAMStream->Initialize(STREAMTYPE_READ, AMMSF_NOGRAPHTHREAD, NULL);
    pAMStream->AddMediaStream(NULL, &MSPID_PrimaryAudio, 0, NULL);
    hr = pAMStream->OpenFile(wszName, AMMSF_RUN);
    {
        if (SUCCEEDED(hr))
        {
            hr = pAMStream->QueryInterface(IID_IMultiMediaStream, 
                (void**)ppMMStream);
        }
    }
    pAMStream->Release();
    return hr;
}

int __cdecl main(int argc, char *argv[])
{
    if (argc < 2)
    {
        printf("Specify a file name.\n");
        exit(0);
    }

    IMultiMediaStream *pMMStream;
    CoInitialize(NULL);
    HRESULT hr = RenderFileToMMStream(argv[1], &pMMStream);
    if (SUCCEEDED(hr))
    {
        RenderStreamToDevice(pMMStream);
        pMMStream->Release();
    }
    
    CoUninitialize();
    return 0;
}


```



## Related topics

<dl> <dt>

[Multimedia Streaming Sample Code](multimedia-streaming-sample-code.md)
</dt> </dl>

 

 



