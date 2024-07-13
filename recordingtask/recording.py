import sounddevice as sd
import scipy.io.wavfile as wav
import matplotlib.pyplot as plt

def list_devices():
    print(sd.query_devices())

def record_voice(duration, filename, device=None):
    sample_rate = 44100  # Standard sample rate for audio

    try:
        # Ensure correct settings for mono/stereo input
        channels = 1  # Change to 1 for mono if needed
        
        # Record audio for the given duration
        print(f"Recording for {duration} seconds on device {device}...")
        audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=channels, device=device)
        sd.wait()  # Wait until the recording is finished
        print("Recording finished!")

        # Save the recorded audio as a WAV file
        wav.write(filename, sample_rate, audio_data)
        print(f"Audio saved as {filename}")

        # Plot the audio data to verify it is not silent
        plt.plot(audio_data)
        plt.title("Recorded Audio Data")
        plt.show()

    except Exception as e:
        print(f"Error recording or saving audio: {e}")

if __name__ == "__main__":
    try:
        # List available devices and get user input
        list_devices()
        duration = float(input("Enter the duration of the recording in seconds: "))
        filename = input("Enter the filename to save the recording (with .wav extension): ")
        device = int(input("Enter the device ID to use for recording: "))

        # Validate the filename (optional)
        if not filename.endswith(".wav"):
            filename += ".wav"  # Ensure the filename ends with .wav

        record_voice(duration, filename, device=device)

    except ValueError:
        print("Invalid input. Please enter a valid number for duration or device ID.")
    except KeyboardInterrupt:
        print("\nRecording interrupted.")
    except Exception as e:
        print(f"Unexpected error: {e}")