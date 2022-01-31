
Fs = 100000; % sampling frequency
Ts = 1/Fs;  
dt = 0:Ts:1-Ts;
w_light = 10000;
w_vibration = 1400;

signal = 1*sin(w_vibration*2*pi*dt)+1*sin(w_light*2*pi*dt)+1.4*cos(2*pi*(w_light+w_vibration)*dt)+1.4*cos(2*pi*(w_light-w_vibration)*dt);
nfft = length(signal);
nfft2 = 2^nextpow2(nfft);
ff = fft(signal,nfft2);
fff = ff(1:nfft2/2);
xfft = Fs*(0:nfft2/2-1)/nfft2;
subplot(2,2,1);

plot(dt,signal);
xlabel('Time(s)');
ylabel('Amplitude (V)');
title('Time domain signal');

subplot(2,1,2);
plot(xfft,abs(fff));
xlabel('Freq(Hz)');
ylabel('Normalized Amplitude');
title('Freq domain signal')
