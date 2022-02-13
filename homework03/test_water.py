import water   

class tests:

    def test_turbid():
        assert water.turbid(3,4) == 12
        assert water.turbid(3,0) == -1
        assert type(water.turbid(3,4)) == float
        assert type(water.turbid(3,0)) == float
        assert water.turbid(-3,4) == -1

    def test_time():
        assert water.time(1,1) == 0.0
        assert type(water.time(1,Ts=0.5)) == float
        assert abs(water.time(40) - 182.5) < 0.5
        assert water.time(1,1,2.0) == -1
        assert water.time(-1) == -1

def run():
    "Run all tests."
    for test in dir(tests):
        item = getattr(tests,test)
        if callable(item) and test.startswith('test'):
            print(item)
            item()

if __name__ == '__main__':
    run()
