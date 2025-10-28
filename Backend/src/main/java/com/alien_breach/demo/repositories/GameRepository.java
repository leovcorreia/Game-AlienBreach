package com.alien_breach.demo.repositories;

import com.alien_breach.demo.models.GameState;
import org.springframework.stereotype.Repository;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.concurrent.ConcurrentHashMap;

@Repository
public class GameRepository {

    private final Map<Long, GameState> games = new ConcurrentHashMap<>();
    private Long nextId = 1L;

    public GameState save(GameState state) {
        if (state.getGameId() == null) {
            state.setGameId(nextId++);
        }
        games.put(state.getGameId(), state);
        return state;
    }

    public GameState findById(Long id) {
        return games.get(id);
    }

    public List<GameState> findAll() {
        return new ArrayList<>(games.values());
    }

    public void delete(Long id) {
        games.remove(id);
    }

}
