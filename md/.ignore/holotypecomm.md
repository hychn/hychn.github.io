# Research Directions and Potential Solutions
* First step, lets try to compile the hololens stuff

# 5.1 Source
## 5.1.1 Representation and Encoding
* MPEG V-PCC, MPEG G-PCC Point cloud compression frameworks 38,39
  * V-PCC encodes point cloud as series of 2D videos
  * G-PCC encodes 3d point cloud data using geometric approaches
* Point cloud encoding takes serveral seconds need to improve existing techologies
  * Use AI to
    1. Increase compression ratio 
    2. Reduce encoding computation complexity
    3. Leverage coordinat between source and destination

## 5.1.2 Mulsemedia synchronization
* Machine learning classifiers and predictors used to verify whether collected senses are consistent and automatically generate senses taht are missing or delayed

# 5.2 Networking
* Semantic communications
  * Accurately transmit communication symbols, addressed by Shannon's communication models
* Text,image,audio. Sense-based semantic communication joint source-channel coding of transmitting text and images 50,53,54
* Environment-based semantic communication: leverage correlations of joint sense information

# 5.2.5 Artificial intelligence: predictive networks and edge intelligence
* Network control and management using model-based solutions, AI provides another solution
* Used for Quality of Service prediction, network planning, network control
* Most existing network protocols respond to abnormal events
  * Predict these events and respond early. Cisco predictive network 72
* Estimate QoS parameers based on partial observation of network status (latency and bandwidth) and determine if the user's requests can e served 73,74
  * RouteNet Graph Neural Networks
* AI can solve complex problems like network planning
  * Deep reinforment learning and graph neural networks are efficient solutions and enable self-driving networking [75]
    * Network Planning with Deep Reinforcement Learning
    * NeuroPlan
* Real-time network control
  * Network monitoring, adapting routine, networking slicing 
    * 76,77,78,79
    * 77 Distrubted multi-hop traffic engineering via stochastic policy gradient reinforcement learning
* user motion prediction to reduce end-to-end latency
* AI-empowered solutions to mitigate impact of prediction errors
* Error detection and correction
  * Missing packets, fading andnoise 84, 85



# 5 Research Directions and Potential Solutions
* Develop efficient hologram encoding and decoding techniques
* Deliver data packets with guaranteed and bounded end-to-end latency that can be defined automatically by users
* Design resilient and intelligent rendering algorithms in presence of packet losses and errors
* Support high-interactive applications

Dear Professor Guo,

I have read the paper on Holographic-Type Communication (HTC). It is an exciting and challenging field.
The high-bandwith and low-lantecy requirements of HTC applications are areas where deep learning can make a significant and meaningful impact.
Here are several thoughts I had.
1. The representation and encoding of point cloud data using deep learning is quite relevant. Many early foundation neural networks (such as U-Net, Transformers, deeplabv3) were sucessful using the encoder-decoder architecture. I think the problem  of encoding and decoding point cloud data will extend well to machine learning.
2. Encoding and decoding messages using semantic communication to minimize semantic errors is an interesting application. The image and text joint coding is very intersting and seems promising.
3. I am not familar with network planning and control. This research sound interesting and is something I am willing to learn. What are your thoughts on this topic?
4. Applying user motion prediction to reduce latency and mitigating errors caused by incorrect prediction, packet loss, or noise are good problems that deep learning can definite address.
5. Alot of the papers mentioned seem to use graph neural networks (GNN). I am familiar with the theory of these networks. It would be nice to practice applying GNNs to reproduce the results of some of the papers.


* This project will mainly focus on how to deliver multimedia content through computer networks and render contents for end XR (AR,MR, VR) users.  You need knowledge from four core areas
* coding: simulation or app development
* machine learning: basic machine learning and deep learning are the foundations of various signal processing. 
* computer networks: effectively capture, deliver and rendering XR contents to end users. 
* multimedia communication: image, video, hologram, multi-sensory


* HoloLens Simulator
  * Hyper-V, windows 10 Education/Professional
