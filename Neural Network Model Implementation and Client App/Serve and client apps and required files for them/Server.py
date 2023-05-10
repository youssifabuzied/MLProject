from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import numpy as np
import pandas as pd
class MyHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = json.loads(self.rfile.read(content_length))

        # Process the received data
        result = process_data(post_data)

        # Send the response
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        response = {'result': result}
        self.wfile.write(json.dumps(response).encode())
def relu(x):
    """
    Computes the element-wise ReLU (rectified linear unit) function on a NumPy array.
    """
    return np.maximum(0, x)
def process_data(data):
    #print(len(data[0]))
    data = np.array(data[0])
    #print(type(data))
    c1 = pd.read_csv("First_Coefecients.csv")
    c1.to_numpy()[:, 1:]
    c1 = c1.iloc[:, 1:]
    c1 = c1.to_numpy()
    b1 = pd.read_csv("Bias1.csv")
    b1 = b1.iloc[:, 1:]
    b1 = b1.to_numpy()
    b2 = pd.read_csv("Bias2.csv")
    b2 = (b2.iloc[:, 1:]).to_numpy()
    r1 = np.dot(data, c1)
    b1 = b1.reshape(1, -1)
    r1 = relu(r1 + b1)
    c2 = pd.read_csv("Second_Coefecients.csv")
    c2 = c2.iloc[:, 1:]
    c2 = c2.to_numpy()
    res = (np.dot(r1, c2) + b2).tolist()
    return res

if __name__ == '__main__':
    server_address = ('localhost', 8000)
    httpd = HTTPServer(server_address, MyHandler)
    print(f'Starting server at http://{server_address[0]}:{server_address[1]}')
    httpd.serve_forever()