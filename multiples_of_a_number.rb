if ARGV.size < 1
    puts "no argument"
else
    Infinity = 1.0/0.0
    File.open(ARGV[0], "r") { |f|
        while line = f.gets
            n = ""
            x = ""
            get_n = false
            line.each_char { |c|
                if get_n
                    n += c
                elsif c == ','
                    get_n = true
                else
                    x += c
                end
            }
            x = x.to_i
            n = n.to_i
            answer = 0
            if n > x
                puts "#{n}"
            else
                (1..Infinity).each { |i|
                    break if answer > x    
                    answer = n * i
                }
            puts "#{answer}"
            end
        end
    }
end
