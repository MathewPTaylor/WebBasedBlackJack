from casinoapp import socketio, app


if __name__ == "__main__":
  socketio.run(app, host='0.0.0.0', port=81, debug=True, use_reloader=False, allow_unsafe_werkzeug=True)